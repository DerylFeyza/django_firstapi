# Generated by Django 5.1.3 on 2024-12-02 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_users_alter_choice_question_question_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Username',
            new_name='username',
        ),
    ]
