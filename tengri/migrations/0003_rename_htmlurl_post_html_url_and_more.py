# Generated by Django 4.2 on 2023-04-21 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tengri', '0002_alter_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='htmlUrl',
            new_name='html_url',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='watchs',
            new_name='watches',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
