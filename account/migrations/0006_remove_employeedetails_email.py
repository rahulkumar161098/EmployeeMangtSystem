# Generated by Django 3.0 on 2022-05-30 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220530_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='email',
        ),
    ]
