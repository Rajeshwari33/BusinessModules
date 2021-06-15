# Generated by Django 3.2 on 2021-05-31 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleDetails', '0005_auto_20210329_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, null=True, verbose_name='User Name')),
                ('mail_id', models.TextField(null=True, verbose_name='Mail Id')),
                ('password', models.CharField(max_length=128, null=True, verbose_name='Password')),
                ('department', models.CharField(max_length=64, null=True, verbose_name='Department')),
                ('reporting_manager', models.CharField(max_length=128, null=True, verbose_name='Reporting Manager')),
                ('user_id', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('creator_id', models.PositiveSmallIntegerField(null=True, verbose_name='Creator Id')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'new_users',
            },
        ),
    ]