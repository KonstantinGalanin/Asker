# Generated by Django 5.0.3 on 2024-03-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0007_remove_profile_like_count_remove_question_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='asker.tag'),
        ),
    ]
