# Generated by Django 4.0.4 on 2022-04-30 17:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_contactus_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Հակիրճ տեքստ')),
                ('large_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Ամբողջական տեքստ')),
            ],
            options={
                'verbose_name': 'Մեր մասին',
                'verbose_name_plural': 'Մեր մասին',
            },
        ),
    ]
