# Generated by Django 5.0.3 on 2024-03-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='img/avatars/'),
        ),
    ]
