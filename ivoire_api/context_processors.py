from django.conf import settings


def site(request):
    context = {
        'site_name': settings.SITE_NAME,
        'admin_url': settings.ADMIN_PAGE_URL,
        'project_mode': settings.PROJECT_DB_MODE,
        'email_host_user': settings.EMAIL_HOST_USER,
    }
    return context
