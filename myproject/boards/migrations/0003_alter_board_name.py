# Generated by Django 4.1.7 on 2023-03-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
