# Generated by Django 5.0.2 on 2024-02-24 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_lesson_video_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]
