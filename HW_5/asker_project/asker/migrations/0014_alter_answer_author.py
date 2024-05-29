# Generated by Django 5.0.3 on 2024-03-30 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0013_alter_answer_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='asker.profile'),
        ),
    ]