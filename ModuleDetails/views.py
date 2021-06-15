from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate
import logging
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db import connection
import pandas as pd
from .send_mail import resend_approved_mail

# Create your views here.

logger = logging.getLogger("business_modules")

@csrf_exempt
def get_user_login(request, *args, **kwargs):
    try:
        if request.method == "POST":
            body = request.body.decode('utf-8')
            data = json.loads(body)

            user_name = ''
            password = ''
            login_time = ''
            system_ip = ''

            for k,v in data.items():
                if k == "username":
                    user_name = v
                if k == "password":
                    password = v
                if k == "login_time":
                    login_time = v
                if k == "system_ip":
                    system_ip = v

            if len(str(user_name)) > 0:
                if len(str(password)) > 0:
                    if len(str(login_time)) > 0:
                        # if len(str(system_ip)) > 0:
                        user = authenticate(request, username = user_name, password = password)
                        if user:
                            users = Users.objects.filter(email=user_name)
                            for user in users:
                                user_id = user.id
                                user_name_login = user.username
                                department_id = user.departments_id

                            departments = Departments.objects.filter(id=department_id)
                            for department in departments:
                                user_department = department.dept_name

                            UserLoginLog.objects.create(
                                system_ip = system_ip,
                                login_time = timezone.now(),
                                users_id = user_id
                            )
                            return JsonResponse({"Status": "Success", "user_id": user_id, "user_name": user_name_login, "department": user_department, "system_ip" : system_ip})
                        else:
                            return JsonResponse({"Status" : "Error", "Message" : "User Not Found!!!"})
                        # else:
                        #     return JsonResponse({"Status" : "Error", "Message" : "System IP not Found!!!"})
                    else:
                        return JsonResponse({"Status" : "Error", "Message" : "Login Time not Found!!!"})
                else:
                    return JsonResponse({"Status" : "Error", "Message" : "Password not Found!!!"})
            else:
                return JsonResponse({"Status" : "Error", "Message" : "Username not Found!!!"})

    except Exception as e:
        logger.error(str(e))
        logger.error("Error in Login User", exc_info=True)
        return JsonResponse({"Status" : "Error"})

@csrf_exempt
def get_user_logout(request, *args, **kwargs):
    try:
        if request.method == "POST":
            body = request.body.decode('utf-8')
            data = json.loads(body)

            system_ip = ''
            user_id = ''

            for k,v in data.items():
                if k == "system_ip":
                    system_ip = v
                if k == "user_id":
                    user_id = v

            if len(str(system_ip)) > 0:
                if len(str(user_id)) > 0:
                    UserLoginLog.objects.create(
                        system_ip=system_ip,
                        logout_time=timezone.now(),
                        users_id=user_id
                    )
                    return JsonResponse({"Status" : "Success"})
                else:
                    return JsonResponse({"Status" : "Error", "Message" : "User Id Not Found!!!"})
            else:
                return JsonResponse({"Status" : "Error", "Message" : "System IP Not Found!!!"})
        else:
            return JsonResponse({"Status" : "Error", "Message" : "POST Method not Received!!!"})
    except Exception as e:
        logger.error(str(e))
        logger.error("Error in Logout User", exc_info=True)
        return JsonResponse({"Status" : "Error"})

@csrf_exempt
def get_user_credentials(request, *args, **kwargs):
    try:
        if request.method == "POST":
            body = request.body.decode('utf-8')
            data = json.loads(body)

            user_id = ''

            for k,v in data.items():
                if k == "user_id":
                    user_id = v

            if len(str(user_id)) > 0:
                # Get the role for the user
                users = Users.objects.filter(id = user_id, is_active = 1)

                for user in users:
                    role_id = user.role_id

                user_role = UserRole.objects.filter(role_id = role_id, is_active = 1)

                tenants_ids = []
                groups_ids = []
                entities_ids = []
                sub_model_ids = []
                module_ids = []

                for role in user_role:
                    tenants_ids.append(role.tenants_id)
                    groups_ids.append(role.groups_id)
                    entities_ids.append(role.entities_id)
                    sub_model_ids.append(role.sub_model_id)
                    module_ids.append(role.module_id)

                # Getting Unique of Tenant, group and entity id
                tenants_id_unique = list(set(tenants_ids))[0]
                groups_id_unique = list(set(groups_ids))[0]
                entities_id_unique = list(set(entities_ids))[0]
                module_ids_unique = list(set(module_ids))[0]

                # List of Ids in Sub Models
                sub_model_ids_unique = list(set(sub_model_ids))

                sub_models_list = []
                main_model_ids = []

                # Creating SubModels List
                for sub_model_id in sub_model_ids_unique:
                    sub_models = SubModels.objects.filter(id = sub_model_id, is_active = 1)

                    for sub_model in sub_models:
                        sub_model_name = sub_model.sub_model_name
                        url_path = sub_model.url_path
                        page_limit = sub_model.page_limit
                        main_model_id = sub_model.main_model_id
                        main_model_ids.append(sub_model.main_model_id) # Getting Main Model ids

                    sub_model_dict = {
                        "sub_model_id" : sub_model_id,
                        "main_model_id" : main_model_id,
                        "sub_model_name" : sub_model_name,
                        "url_path" : url_path,
                        "page_limit" : page_limit
                    }
                    sub_models_list.append(sub_model_dict)

                # Creating Main Models List
                main_model_ids_unique = list(set(main_model_ids))
                main_models_list = []

                for main_model_id in main_model_ids_unique:
                    main_models = MainModels.objects.filter(id = main_model_id, is_active = 1)

                    for main_model in main_models:
                        model_name = main_model.model_name

                    main_model_dict = {
                        "main_model_id" : main_model_id,
                        "module_name" : model_name
                    }

                    main_models_list.append(main_model_dict)

                tenants = Tenants.objects.filter(id = tenants_id_unique)

                for tenant in tenants:
                    tenant_code = tenant.tenant_code

                tenant_extension = tenant_code.split("@")[-1]

                return JsonResponse({
                    "main_models" : main_models_list,
                    "sub_models" : sub_models_list,
                    "tenant_id" : tenants_id_unique,
                    "group_id" : groups_id_unique,
                    "entity_id" : entities_id_unique,
                    "module_id" : module_ids_unique,
                    "tenant_extension" : tenant_extension
                })
            else:
                return JsonResponse({"Status" : "Error", "Message" : "User Id Not Found!!!"})

    except Exception as e:
        logger.error(str(e))
        logger.error("Error in Getting User Credentials", exc_info=True)
        return JsonResponse({"Status": "Error"})

def execute_sql_query(query, object_type):
    try:
        with connection.cursor() as cursor:
            logger.info("Executing SQL Query..")
            logger.info(query)

            cursor.execute(query)
            if object_type == "table":
                column_names = [col[0] for col in cursor.description]
                rows = dict_fetch_all(cursor)
                table_output = {"headers": column_names, "data": rows}
                output = json.dumps(table_output)
                return output
            elif object_type in ["update", "create"]:
                return None
            else:
                rows = cursor.fetchall()
                column_header = [col[0] for col in cursor.description]
                df = pd.DataFrame(rows)
                return [df, column_header]

    except Exception as e:
        logger.info("Error Executing SQL Query!!", exc_info=True)
        return None


def dict_fetch_all(cursor):
    "Return all rows from cursor as a dictionary"
    try:
        column_header = [col[0] for col in cursor.description]
        return [dict(zip(column_header, row)) for row in cursor.fetchall()]
    except Exception as e:
        logger.error("Error in converting cursor data to dictionary", exc_info=True)

@csrf_exempt
def new_users_list(request, *args, **kwargs):
    try:
        if request.method == "POST":
            body = request.body.decode('utf-8')
            data = json.loads(body)

            for k,v in data.items():
                if k == "user_id":
                    user_id = v

            # values = NewUsers.objects.filter(creator_id=user_id)
            # for value in values:
            if user_id == 24:
                query = "SELECT user_name, mail_id, department, reporting_manager, user_id FROM business_modules.new_users WHERE is_active = 0;"
                query_output = json.loads(execute_sql_query(query, object_type="table"))

                active_query = "SELECT user_name, mail_id, department, reporting_manager, user_id FROM business_modules.new_users WHERE is_active = 1;"
                active_query_output = json.loads(execute_sql_query(active_query, object_type="table"))

                return JsonResponse({
                    "user_list" : query_output["data"],
                    "active_list" : active_query_output["data"]
                })
            else:
                return JsonResponse({"Status" : "Error", "Message" : "User Id Not Found!!!"})

        else:
            return JsonResponse({"Status" : "Error", "Message" : "POST Method Not Received!!"})
    except Exception as e:
        logger.error(str(e))
        logger.error("Error in Getting New Users List", exc_info=True)
        return JsonResponse({"Status" : "Error"})

@csrf_exempt
def create_user_temp(request, *args, **kwargs):
    try:
        if request.method == "POST":
            body = request.body.decode('utf-8')
            data = json.loads(body)

            for k, v in data.items():
                if k == "mail_id":
                    mail_id = v
                if k == "user_id":
                    user_id = v

            if len(str(mail_id)) > 0:
                if len(str(user_id)) > 0:

                    details = Users.objects.filter(id=user_id)
                    for detail in details:
                        detail.is_active = 1
                        detail.save()

                    values = NewUsers.objects.filter(mail_id=mail_id, user_id=user_id)
                    for value in values:
                        value.is_active = 1
                        value.save()
                        mail_id = value.mail_id
                        password1 = value.password
                        user_name = value.user_name
                        from_mail_id = "rajichawla0925@gmail.com"
                        password = "Ponn1234@raj"
                        link = "http://154.61.75.57:4201"
                        subject = "Create Your PRF"
                        body = "Dear" + " " + user_name + "," + """\n""" + """You can create your PRF by using below link and mail credentials.""" + """\n\n""" + """Application Link - """ + link + """\n""" + """Mail Id - """ + mail_id + """\n""" + """Password""" + password1 + """\n\n""" + """Thanks and Regards""" + """\n""" + """Teamlease Services Limited"""
                        if (resend_approved_mail(mail_id, body, subject, from_mail_id, password)):

                            logger.info("Create PRF Email send to the Department Head")
                            # print("Success")
                        #     logger.info(customer_mail_id)
                        else:
                            logger.error("Create PRF Email Not sent to the Depatment Head")

                    return  JsonResponse({"Status" : "Success", "Message" : "User Created Successfully!!!"})
                else:
                    return JsonResponse({"Status": "Error", "Message": "User Id Not Found!!!"})
            else:
                return JsonResponse({"Status": "Error", "Message": "User Name Not Found!!!"})
        else:
            return JsonResponse({"Status" : "Error", "Message" : "POST Method Not Recieved!!!"})
    except Exception as e:
        logger.error(str(e))
        logger.error("Error in Creating New User", exc_info=True)
        return JsonResponse({"Status" : "Error"})


@csrf_exempt
def remove_user_temp(request, *args, **kwargs):
    try:
        if request.method == "POST":
            body = request.body.decode('utf-8')
            data = json.loads(body)

            for k, v in data.items():
                if k == "mail_id":
                    mail_id = v
                if k == "user_id":
                    user_id = v

            if len(str(mail_id)) > 0:
                if len(str(user_id)) > 0:

                    details = Users.objects.filter(email=mail_id, id=user_id)
                    for detail in details:
                        detail.is_active = 0
                        detail.save()

                    values = NewUsers.objects.filter(mail_id=mail_id, user_id=user_id)
                    for value in values:
                        value.is_active = 0
                        value.save()
                    return JsonResponse({"Status": "Success", "Message": "User Removed Successfully!!!"})
                else:
                    return JsonResponse({"Status": "Error", "Message": "User Id Not Found!!!"})
            else:
                return JsonResponse({"Status": "Error", "Message": "User Name Not Found!!!"})
        else:
            return JsonResponse({"Status": "Error", "Message": "POST Method Not Recieved!!!"})

    except Exception as e:
        logger.error(str(e))
        logger.error("Error in Creating New User", exc_info=True)
        return JsonResponse({"Status": "Error"})