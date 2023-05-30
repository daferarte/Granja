# Generated by Django 4.2 on 2023-05-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Productor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cedula", models.CharField(max_length=40, verbose_name="Cedula")),
                ("nombres", models.CharField(max_length=150, verbose_name="Nombres")),
                (
                    "apellidos",
                    models.CharField(max_length=150, verbose_name="Apellidos"),
                ),
                (
                    "direccion",
                    models.CharField(max_length=150, verbose_name="Direccion"),
                ),
                (
                    "fNacimiento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de cumpleaños"
                    ),
                ),
                (
                    "telefono",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Teléfono"
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="Editado"),
                ),
            ],
            options={
                "verbose_name": "Productor",
                "verbose_name_plural": "Productores",
            },
        ),
    ]