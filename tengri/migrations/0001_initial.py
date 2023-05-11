# Generated by Django 4.2 on 2023-04-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_created=True, help_text='Time of publish')),
                ('title', models.CharField(help_text='Name of post', max_length=200)),
                ('htmlUrl', models.CharField(help_text='That is a path to html', max_length=200)),
                ('watchs', models.IntegerField()),
            ],
        ),
    ]