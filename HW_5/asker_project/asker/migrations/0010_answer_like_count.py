# Generated by Django 5.0.3 on 2024-03-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0009_question_answer_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
