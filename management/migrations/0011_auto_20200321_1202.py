# Generated by Django 3.0.4 on 2020-03-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20200321_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposalstate',
            name='proposal',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='ProposalState',
        ),
    ]
