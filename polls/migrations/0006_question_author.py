# Generated by Django 5.1.3 on 2024-12-05 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_question_user_delete_user'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created', to='user.user'),
            preserve_default=False,
        ),
    ]