# Generated by Django 3.0.4 on 2020-03-19 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(help_text='Nome do Fornecedor', max_length=128)),
                ('product_type', models.CharField(help_text='EPI/Ventilador', max_length=128)),
            ],
        ),
    ]