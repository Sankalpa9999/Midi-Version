# Generated by Django 5.0.3 on 2024-07-08 05:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
        ('Exercise', '0004_alter_exercise_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_workouts', to='Exercise.exercise'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_workouts', to=settings.AUTH_USER_MODEL),
        ),
    ]
