# Generated by Django 4.2.1 on 2024-03-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prompt_studio_core", "0005_alter_customtool_default_profile_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customtool",
            name="summarize_as_source",
            field=models.BooleanField(
                db_comment="Flag to use summarized content as source", default=False
            ),
        ),
        migrations.AlterField(
            model_name="customtool",
            name="summarize_context",
            field=models.BooleanField(
                db_comment="Flag to summarize content", default=False
            ),
        ),
    ]