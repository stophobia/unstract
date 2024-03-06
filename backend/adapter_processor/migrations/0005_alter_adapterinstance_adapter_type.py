# Generated by Django 4.2.1 on 2024-02-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adapter_processor", "0004_alter_adapterinstance_adapter_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adapterinstance",
            name="adapter_type",
            field=models.CharField(
                choices=[
                    ("UNKNOWN", "UNKNOWN"),
                    ("LLM", "LLM"),
                    ("EMBEDDING", "EMBEDDING"),
                    ("VECTOR_DB", "VECTOR_DB"),
                    ("OCR", "OCR"),
                    ("X2TEXT", "X2TEXT"),
                ],
                db_comment="Type of adapter LLM/EMBEDDING/VECTOR_DB",
            ),
        ),
    ]