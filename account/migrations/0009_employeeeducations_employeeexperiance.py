# Generated by Django 3.0 on 2022-05-30 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0008_auto_20220530_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeExperiance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company2_name', models.CharField(max_length=200, null=True)),
                ('company2_desg', models.CharField(max_length=200, null=True)),
                ('company2_duration', models.CharField(max_length=60, null=True)),
                ('company1_name', models.CharField(max_length=200, null=True)),
                ('company1_desg', models.CharField(max_length=200, null=True)),
                ('company1_duration', models.CharField(max_length=60, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEducations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_pg', models.CharField(max_length=200, null=True)),
                ('college_name_pg', models.CharField(max_length=200, null=True)),
                ('pass_year_pg', models.CharField(max_length=60, null=True)),
                ('parcentage_pg', models.CharField(max_length=50, null=True)),
                ('course_ug', models.CharField(max_length=200, null=True)),
                ('college_name_ug', models.CharField(max_length=200, null=True)),
                ('pass_year_ug', models.CharField(max_length=60, null=True)),
                ('parcentage_ug', models.CharField(max_length=50, null=True)),
                ('course_ssc', models.CharField(max_length=200, null=True)),
                ('college_name_scc', models.CharField(max_length=200, null=True)),
                ('pass_year_ssc', models.CharField(max_length=60, null=True)),
                ('parcentage_ssc', models.CharField(max_length=50, null=True)),
                ('course_hc', models.CharField(max_length=200, null=True)),
                ('college_name_hc', models.CharField(max_length=200, null=True)),
                ('pass_year_hc', models.CharField(max_length=60, null=True)),
                ('parcentage_hc', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
