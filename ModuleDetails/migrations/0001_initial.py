# Generated by Django 3.1.7 on 2021-03-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=64, verbose_name='Department Code')),
                ('dept_name', models.CharField(max_length=64, verbose_name='Department Name')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Entities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_code', models.CharField(max_length=64, unique=True, verbose_name='Entity Code')),
                ('entity_name', models.CharField(max_length=64, unique=True, verbose_name='Entity Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'entities',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_code', models.CharField(max_length=64, unique=True, verbose_name='Group Code')),
                ('group_name', models.CharField(max_length=64, unique=True, verbose_name='Group Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='MainModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=128, null=True, unique=True, verbose_name='Icon')),
                ('module_code', models.CharField(max_length=64, unique=True, verbose_name='Module Code')),
                ('module_name', models.CharField(max_length=64, unique=True, verbose_name='Module Name')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('modified_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified Date')),
            ],
            options={
                'db_table': 'main_models',
            },
        ),
        migrations.CreateModel(
            name='MainModules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=128, null=True, unique=True, verbose_name='Icon')),
                ('module_code', models.CharField(max_length=64, unique=True, verbose_name='Module Code')),
                ('module_name', models.CharField(max_length=64, unique=True, verbose_name='Module Name')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('modified_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified Date')),
            ],
            options={
                'db_table': 'main_modules',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_code', models.CharField(max_length=64, verbose_name='Role Code')),
                ('role_name', models.CharField(max_length=64, verbose_name='Role Name')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='SubModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_module_code', models.CharField(max_length=64, unique=True, verbose_name='Sub Module Code')),
                ('sub_module_name', models.CharField(max_length=64, unique=True, verbose_name='Sub Module Name')),
                ('sub_module_status', models.BooleanField(default=True, verbose_name='Sub Module Status')),
                ('url_path', models.CharField(max_length=64, null=True, unique=True, verbose_name='URL Path')),
                ('page_limit', models.PositiveSmallIntegerField(verbose_name='Page Limit')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('modified_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified Date')),
                ('main_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.mainmodules', verbose_name='Main Model Id (Auto Generated)')),
            ],
            options={
                'db_table': 'sub_models',
            },
        ),
        migrations.CreateModel(
            name='SubModules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_module_code', models.CharField(max_length=64, unique=True, verbose_name='Sub Module Code')),
                ('sub_module_name', models.CharField(max_length=64, unique=True, verbose_name='Sub Module Name')),
                ('sub_module_status', models.BooleanField(default=True, verbose_name='Sub Module Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('modified_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified Date')),
                ('main_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.mainmodules', verbose_name='Main Module Id (Auto Generated)')),
            ],
            options={
                'db_table': 'module',
            },
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_code', models.CharField(max_length=64, unique=True, verbose_name='Tenant Code')),
                ('tenant_name', models.CharField(max_length=64, unique=True, verbose_name='Tenant Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'tenants',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Email Id')),
                ('username', models.CharField(max_length=64, verbose_name='User Name')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Is Approved ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('modified_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified Date')),
                ('departments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.departments', verbose_name='Departments Id (Auto Generated)')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.roles', verbose_name='Role Id (Auto Generated)')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('created_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('modified_by', models.PositiveSmallIntegerField(null=True, verbose_name='User Id')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified Date')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.departments', verbose_name='Department Id (Auto Generated)')),
                ('entities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.entities', verbose_name='Entities Id (Auto Generated)')),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.groups', verbose_name='Groups Id (Auto Generated)')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.submodules', verbose_name='Module Id (Auto Generated)')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.roles', verbose_name='Roles Id (Auto Generated)')),
                ('sub_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.submodels', verbose_name='Sub Model Id (Auto Generated)')),
                ('tenants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.tenants', verbose_name='Tenants Id (Auto Generated)')),
            ],
            options={
                'db_table': 'user_role',
            },
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_ip', models.CharField(max_length=32, null=True, verbose_name='System IP Address')),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Login Time')),
                ('logout_time', models.DateTimeField(null=True, verbose_name='Logout Time')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Users Id (Auto Generated)')),
            ],
            options={
                'db_table': 'user_login_log',
            },
        ),
        migrations.AddField(
            model_name='groups',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.tenants', verbose_name='Tenants Id (Auto Generated)'),
        ),
        migrations.AddField(
            model_name='entities',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.groups', verbose_name='Groups Id (Auto Generated)'),
        ),
        migrations.AddField(
            model_name='departments',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModuleDetails.entities', verbose_name='Entity Id (Auto Generated'),
        ),
    ]
