# Generated by Django 3.2.8 on 2021-11-02 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_home', '0002_card_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('subtitle', models.TextField()),
            ],
        ),
    ]