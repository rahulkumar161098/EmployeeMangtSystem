# Generated by Django 3.0 on 2022-05-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20220530_0823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetails',
            old_name='gender',
            new_name='emp_gender',
        ),
    ]
