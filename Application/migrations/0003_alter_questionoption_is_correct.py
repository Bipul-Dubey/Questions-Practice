# Generated by Django 4.1.2 on 2022-11-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Application", "0002_questionoption_is_correct_delete_correctoption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionoption",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
    ]
