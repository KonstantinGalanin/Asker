# Generated by Django 5.0.3 on 2024-05-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0019_answer_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
