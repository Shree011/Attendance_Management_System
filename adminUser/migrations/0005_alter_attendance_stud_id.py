# Generated by Django 4.0.2 on 2022-04-15 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminUser', '0004_rename_roll_no_attendance_stud_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='stud_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminUser.student'),
        ),
    ]
