# Generated by Django 4.1.5 on 2023-01-24 13:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='uploads/domain')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be start with: '09'", regex='^09[0-9]{8}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter_app.section')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='uploads/article/image')),
                ('article_file', models.FileField(upload_to='uploads/article/file')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter_app.domain')),
                ('publisher', models.ManyToManyField(to='newsletter_app.publisher')),
            ],
        ),
    ]
