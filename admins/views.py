from django.shortcuts import render
from users.models import User

def index(request):
    return render(request, 'admins/index.html')


def admin_users(request):
    context = {'title': 'Админ-панель - Пользовтаели', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')

def admin_users_update_delete(request):
    return render(request, 'admin/admin-users-update-delete')

