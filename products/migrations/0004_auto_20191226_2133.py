# Generated by Django 2.0.2 on 2019-12-27 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='hunter',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='product',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
