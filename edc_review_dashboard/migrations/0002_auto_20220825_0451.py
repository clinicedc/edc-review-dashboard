# Generated by Django 3.2.13 on 2022-08-25 01:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edc_review_dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ReviewDashboard",
            new_name="EdcPermissions",
        ),
        migrations.AlterModelOptions(
            name="edcpermissions",
            options={
                "verbose_name": "Edc Permissions",
                "verbose_name_plural": "Edc Permissions",
            },
        ),
    ]
