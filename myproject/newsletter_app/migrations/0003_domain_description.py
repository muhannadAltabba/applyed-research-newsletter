# Generated by Django 4.1.5 on 2023-01-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0002_rename_title_domain_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
