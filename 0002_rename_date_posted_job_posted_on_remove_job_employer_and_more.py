# Generated by Django 5.1.4 on 2024-12-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="date_posted",
            new_name="posted_on",
        ),
        migrations.RemoveField(
            model_name="job",
            name="employer",
        ),
        migrations.AddField(
            model_name="job",
            name="company",
            field=models.CharField(default="Unknown Company", max_length=100),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
