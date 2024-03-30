# Generated by Django 5.0.3 on 2024-03-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0006_remove_tag_questions_question_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(related_name='tag', to='asker.question'),
        ),
    ]