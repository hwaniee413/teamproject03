# Generated by Django 4.1.6 on 2023-03-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0003_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('runtime', models.CharField(max_length=15)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
