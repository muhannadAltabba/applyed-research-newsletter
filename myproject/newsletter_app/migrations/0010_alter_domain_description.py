# Generated by Django 4.1.5 on 2023-02-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0009_rename_description_article_abstruct_problem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
    ]
