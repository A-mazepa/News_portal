# Generated by Django 4.1 on 2022-08-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NewsApp", "0003_rename_user_commemt_comment_user_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="rating_comment",
            field=models.FloatField(default=0.0),
        ),
    ]
