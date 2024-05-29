from django.shortcuts import render
from django.urls import reverse
from .models import Venda, Produto
from .forms import VendaForm, ItemVendaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User


@login_required
def index(request):
    return render(request, 'venda/index.html')


@login_required
def list_venda(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    vendas = usuario.vendas.order_by('id')
    context = {'vendas': vendas}
    return render(request, 'venda/list_venda.html', context)


@login_required
def detail_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    itens_venda = venda.itens_venda.order_by('quantidade')
    context = {'venda': venda, 'itens_venda': itens_venda}
    return render(request, 'venda/detail_venda.html', context)


@login_required
def list_usuarios(request):
    if not request.user.is_superuser:
        raise Http404
    usuarios = User.objects.order_by('id')
    context = {'usuarios': usuarios}
    return render(request, 'venda/list_clientes.html', context)


@login_required
def list_produtos(request):
    produtos = Produto.objects.order_by('id')
    context = {'produtos': produtos}
    return render(request, 'venda/list_produtos.html', context)


def cadastrarVenda(request):
    if request.method != 'POST':
        formVenda = VendaForm()
        formItemVenda = ItemVendaForm()
    else:
        formVenda = VendaForm(request.POST)
        formItemVenda = ItemVendaForm(request.POST)
        if formVenda.is_valid() and formItemVenda.is_valid():
            venda = formVenda.save()
            itemVenda = formItemVenda.save(commit=False)
            itemVenda.venda = venda
            itemVenda.save()
            return HttpResponseRedirect(reverse('index'))

    context = {'formVenda': formVenda, 'formItemVenda': formItemVenda}
    return render(request, 'venda/cadastrarVenda.html', context)
