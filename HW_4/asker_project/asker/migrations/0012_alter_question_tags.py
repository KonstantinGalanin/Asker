# Generated by Django 5.0.3 on 2024-03-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0011_question_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='questions', to='asker.tag'),
        ),
    ]
