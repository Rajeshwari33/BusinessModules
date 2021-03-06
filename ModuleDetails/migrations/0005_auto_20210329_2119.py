# Generated by Django 3.1.7 on 2021-03-29 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleDetails', '0004_auto_20210329_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainmodels',
            old_name='module_code',
            new_name='model_code',
        ),
        migrations.RenameField(
            model_name='mainmodels',
            old_name='module_name',
            new_name='model_name',
        ),
        migrations.RenameField(
            model_name='submodels',
            old_name='main_module',
            new_name='main_model',
        ),
        migrations.RenameField(
            model_name='submodels',
            old_name='sub_module_code',
            new_name='sub_model_code',
        ),
        migrations.RenameField(
            model_name='submodels',
            old_name='sub_module_name',
            new_name='sub_model_name',
        ),
        migrations.RenameField(
            model_name='submodels',
            old_name='sub_module_status',
            new_name='sub_model_status',
        ),
    ]
