from django.shortcuts import render
from django.shortcuts import render
from .models import Users
from .forms import UserForm
import hashlib

def hash(message):
    hash_object_md5 = hashlib.md5(message.encode())
    md5_hash = hash_object_md5.hexdigest()
    return md5_hash
def upcase_first_letter(s):
    return s[0].upper() + s[1:]
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = upcase_first_letter(form.cleaned_data.get('username'))
            password = hash(form.cleaned_data.get('password'))

            # Запрос к базе данных для проверки наличия пользователя и правильности пароля
            try:

                user_data = Users.objects.filter(username=username, password=password)
                # Если пользователь существует и пароль верен, выполните необходимые действия
                return render(request, 'code.html', {'user': user_data})

            except Users.DoesNotExist:
                # Обработка случая, когда пользователь не найден или пароль неверен
                return render(request, 'error.html',
                              {'message': 'Неверное имя пользователя или пароль'})

    else:
        form = UserForm()

    return render(request, 'auth.html', {'form': form})
# Create your views here.
