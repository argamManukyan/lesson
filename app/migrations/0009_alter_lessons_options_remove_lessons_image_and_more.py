# Generated by Django 4.0.4 on 2022-05-08 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_classes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name': 'Դաս', 'verbose_name_plural': 'Դասեր'},
        ),
        migrations.RemoveField(
            model_name='lessons',
            name='image',
        ),
        migrations.DeleteModel(
            name='LessonImages',
        ),
    ]
