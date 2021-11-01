# Generated by Django 3.2.8 on 2021-11-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('link', models.URLField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]