# Generated by Django 3.0.2 on 2020-02-08 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants_home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='prod_id',
        ),
    ]