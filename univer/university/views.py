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

            try:

                user_data = Users.objects.filter(username=username, password=password)
                print(username, password)
                if user_data:
                    return render(request, 'code.html', {'user': user_data})
                else: return render(request, 'auth.html',{'form': form,
                                                    'error': 'Неверное имя пользователя или пароль'})


            except Exception as e:
                return render(request, 'error.html',{'error': e})

    else:
        form = UserForm()

    return render(request, 'auth.html', {'form': form})

