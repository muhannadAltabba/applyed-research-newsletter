# Generated by Django 4.1.5 on 2023-01-31 07:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0005_alter_article_article_file_alter_article_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be start with: '09'", regex='^09[0-9]{8}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sharepoint', models.CharField(max_length=200)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter_app.section')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='article',
            name='publisher',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_file',
            field=models.FileField(upload_to='article/file'),
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(upload_to='article/image'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='photo',
            field=models.ImageField(upload_to='domain'),
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.AddField(
            model_name='article',
            name='contributor',
            field=models.ManyToManyField(to='newsletter_app.contributor'),
        ),
    ]
