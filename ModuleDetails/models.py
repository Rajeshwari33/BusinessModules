from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django_mysql.models import JSONField

# Create your models here.

class Tenants(models.Model):
    class Meta:
        db_table = "tenants"

    tenant_code = models.CharField(max_length=64, verbose_name="Tenant Code", null=False, unique=True)
    tenant_name = models.CharField(max_length=64, verbose_name="Tenant Name", null=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")

class Groups(models.Model):
    class Meta:
        db_table = "groups"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenants Id (Auto Generated)", on_delete=models.CASCADE)
    group_code = models.CharField(max_length=64, verbose_name="Group Code", null=False, unique=True)
    group_name = models.CharField(max_length=64, verbose_name="Group Name", null=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")

class Entities(models.Model):
    class Meta:
        db_table = "entities"

    group = models.ForeignKey(Groups, verbose_name="Groups Id (Auto Generated)", on_delete=models.CASCADE)
    entity_code = models.CharField(max_length=64, verbose_name="Entity Code", null=False, unique=True)
    entity_name = models.CharField(max_length=64, verbose_name="Entity Name", null=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")

class Departments(models.Model):
    class Meta:
        db_table = "departments"

    entity = models.ForeignKey(Entities, verbose_name="Entity Id (Auto Generated", on_delete=models.CASCADE)
    dept_code = models.CharField(max_length=64, verbose_name="Department Code", null=False)
    dept_name = models.CharField(max_length=64, verbose_name="Department Name", null=False)
    status = models.BooleanField(default=True, verbose_name="Status")
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")

class Roles(models.Model):
    class Meta:
        db_table = "roles"

    role_code = models.CharField(max_length=64, verbose_name="Role Code", null=False)
    role_name = models.CharField(max_length=64, verbose_name="Role Name", null=False)
    status = models.BooleanField(default=True, verbose_name="Status")
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")

class UserManager(BaseUserManager):

    def create_superuser(self, email, password, username, role, departments):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            role_id = role,
            departments_id = departments
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "users"

    role = models.ForeignKey(Roles, verbose_name="Role Id (Auto Generated)", on_delete=models.CASCADE)
    departments = models.ForeignKey(Departments, verbose_name="Departments Id (Auto Generated)", on_delete=models.CASCADE)
    email = models.EmailField(max_length=128, unique=True, verbose_name="Email Id")
    username = models.CharField(max_length=64, verbose_name="User Name")
    is_approved = models.BooleanField(default=False, verbose_name="Is Approved ?")
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    modified_by = models.PositiveSmallIntegerField( verbose_name="User Id", null=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name="Modified Date")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role', 'departments']

    objects = UserManager()

class MainModules(models.Model):
    class Meta:
        db_table = "main_modules"

    module_code = models.CharField(max_length=64, verbose_name="Module Code", null=False, unique=True)
    module_name = models.CharField(max_length=64, verbose_name="Module Name", null=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    modified_by = models.PositiveSmallIntegerField( verbose_name="User Id", null=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name="Modified Date")

class SubModules(models.Model):
    class Meta:
        db_table = "sub_module"

    main_module = models.ForeignKey(MainModules, verbose_name="Main Module Id (Auto Generated)", on_delete=models.CASCADE)
    sub_module_code = models.CharField(max_length=64, verbose_name="Sub Module Code", null=False, unique=True)
    sub_module_name = models.CharField(max_length=64, verbose_name="Sub Module Name", null=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    modified_by = models.PositiveSmallIntegerField( verbose_name="User Id", null=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name="Modified Date")

class MainModels(models.Model):
    class Meta:
        db_table = "main_models"

    icon = models.CharField(max_length=128, verbose_name="Icon", null=True, unique=True)
    model_code = models.CharField(max_length=64, verbose_name="Module Code", null=False, unique=True)
    model_name = models.CharField(max_length=64, verbose_name="Module Name", null=False, unique=True)
    status = models.BooleanField(default=True, verbose_name="Status")
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    modified_by = models.PositiveSmallIntegerField( verbose_name="User Id", null=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name="Modified Date")

class SubModels(models.Model):
    class Meta:
        db_table = "sub_models"

    main_model = models.ForeignKey(MainModules, verbose_name="Main Model Id (Auto Generated)", on_delete=models.CASCADE)
    sub_model_code = models.CharField(max_length=64, verbose_name="Sub Module Code", null=False, unique=True)
    sub_model_name = models.CharField(max_length=64, verbose_name="Sub Module Name", null=False, unique=True)
    sub_model_status = models.BooleanField(default=True, verbose_name="Sub Module Status")
    url_path = models.CharField(max_length=64, verbose_name="URL Path", null=True, unique=True)
    page_limit = models.PositiveSmallIntegerField(verbose_name="Page Limit", null=False)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    modified_by = models.PositiveSmallIntegerField( verbose_name="User Id", null=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name="Modified Date")

class UserRole(models.Model):
    class Meta:
        db_table = "user_role"

    sub_model = models.ForeignKey(SubModels, verbose_name="Sub Model Id (Auto Generated)", on_delete=models.CASCADE)
    module = models.ForeignKey(SubModules, verbose_name="Module Id (Auto Generated)", on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, verbose_name="Roles Id (Auto Generated)", on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, verbose_name="Department Id (Auto Generated)", on_delete=models.CASCADE)
    tenants = models.ForeignKey(Tenants, verbose_name="Tenants Id (Auto Generated)", on_delete=models.CASCADE)
    groups = models.ForeignKey(Groups, verbose_name="Groups Id (Auto Generated)", on_delete=models.CASCADE)
    entities = models.ForeignKey(Entities, verbose_name="Entities Id (Auto Generated)", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    modified_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name="Modified Date")

class UserLoginLog(models.Model):
    class Meta:
        db_table = "user_login_log"

    users = models.ForeignKey(Users, verbose_name="Users Id (Auto Generated)", on_delete=models.CASCADE)
    system_ip = models.CharField(max_length = 32, verbose_name="System IP Address", null=True)
    login_time = models.DateTimeField(default=timezone.now, verbose_name="Login Time", null=False)
    logout_time = models.DateTimeField(verbose_name="Logout Time", null=True)

class NewUsers(models.Model):
    class Meta:
        db_table = "new_users"

    user_name = models.CharField(max_length=255, verbose_name="User Name", null=True)
    mail_id = models.TextField(verbose_name="Mail Id", null=True)
    password = models.CharField(max_length=128, verbose_name="Password", null=True)
    department = models.CharField(max_length=64, verbose_name="Department", null=True)
    reporting_manager = models.CharField(max_length=128, verbose_name="Reporting Manager", null=True)
    user_id = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    creator_id = models.PositiveSmallIntegerField(verbose_name="Creator Id", null=True)
    is_active = models.BooleanField(default=True, verbose_name="Active ?")
    created_by = models.PositiveSmallIntegerField(verbose_name="User Id", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created Date")