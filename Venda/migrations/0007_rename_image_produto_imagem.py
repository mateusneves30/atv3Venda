# Generated by Django 5.0.6 on 2024-06-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Venda', '0006_produto_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image',
            new_name='imagem',
        ),
    ]
