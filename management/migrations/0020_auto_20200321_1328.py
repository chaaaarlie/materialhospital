# Generated by Django 3.0.4 on 2020-03-21 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_auto_20200321_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='management.ProductType'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='type',
            field=models.CharField(blank=True, choices=[('E', 'Equipamento Protecao Individual'), ('V', 'Ventilador'), ('T', 'Kit Teste')], default=None, help_text='Tipo de Produto', max_length=32),
        ),
    ]
