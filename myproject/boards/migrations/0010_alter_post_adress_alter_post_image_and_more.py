# Generated by Django 4.1.7 on 2023-04-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0009_topic_adress_topic_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Adress',
            field=models.TextField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='topic',
            name='Adress',
            field=models.TextField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]