# Generated by Django 4.1.7 on 2023-04-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_alter_post_adress_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]