# Generated by Django 3.0.4 on 2020-03-21 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20200321_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_subtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.ProductSubType'),
        ),
    ]
