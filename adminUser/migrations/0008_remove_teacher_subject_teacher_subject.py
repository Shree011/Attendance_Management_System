# Generated by Django 4.0.2 on 2022-04-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUser', '0007_subject_remove_teacher_subject_teacher_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]