# Generated by Django 4.2 on 2023-05-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finca", "0002_recoleccion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recoleccion",
            name="novedad",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="novedad"
            ),
        ),
    ]
