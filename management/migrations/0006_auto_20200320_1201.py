# Generated by Django 3.0.4 on 2020-03-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20200320_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='supplier',
        ),
        migrations.AlterField(
            model_name='proposal',
            name='picture',
            field=models.ImageField(height_field='height', upload_to='./uploads/images/<property object at 0x7f2fe1542548>/', width_field='width'),
        ),
    ]
