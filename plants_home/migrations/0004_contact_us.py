# Generated by Django 3.0.2 on 2020-02-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_home', '0003_auto_20200208_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('contact_number', models.CharField(blank=True, max_length=10)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='contact_us/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
