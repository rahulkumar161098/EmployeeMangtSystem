# Generated by Django 3.0 on 2022-05-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_employeedetails_emp_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='mobile',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
