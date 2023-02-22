# Generated by Django 4.1.5 on 2023-01-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0003_domain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_file',
            field=models.FileField(upload_to='newsletter_app/uploads/article/file'),
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(upload_to='newsletter_app/uploads/article/image'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='photo',
            field=models.ImageField(upload_to='newsletter_app/uploads/domain'),
        ),
    ]