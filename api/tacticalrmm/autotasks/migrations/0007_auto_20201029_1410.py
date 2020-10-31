# Generated by Django 3.1.2 on 2020-10-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autotasks", "0006_auto_20200922_1344"),
    ]

    operations = [
        migrations.AddField(
            model_name="automatedtask",
            name="remove_if_not_scheduled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="automatedtask",
            name="run_time_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="automatedtask",
            name="task_type",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled"),
                    ("checkfailure", "On Check Failure"),
                    ("manual", "Manual"),
                    ("runonce", "Run Once"),
                ],
                default="manual",
                max_length=100,
            ),
        ),
    ]
