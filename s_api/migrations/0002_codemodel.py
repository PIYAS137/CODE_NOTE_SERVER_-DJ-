# Generated by Django 5.0.4 on 2024-05-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10000)),
                ('s_id', models.IntegerField()),
                ('s_secret', models.IntegerField()),
                ('date', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=40)),
            ],
        ),
    ]