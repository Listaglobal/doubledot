# Generated by Django 4.2.2 on 2023-08-19 18:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_post_status_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('885cbac5-944b-42b5-bd70-b6ba6dfe1197'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
