# Generated by Django 5.1.3 on 2024-12-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='expires_at',
            field=models.DateTimeField(null=True),
        ),
    ]
