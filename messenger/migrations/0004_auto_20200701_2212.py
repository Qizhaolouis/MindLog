# Generated by Django 3.0.5 on 2020-07-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_auto_20200628_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sender',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
