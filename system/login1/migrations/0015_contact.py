# Generated by Django 3.2.6 on 2021-09-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0014_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]
