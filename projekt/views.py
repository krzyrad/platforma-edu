#Widoki dla aplikacji portal.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistration, StudentRegistration
from portal.models import Student, User
"""from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contri.auth import logout"""
#Widok dla strony logowania.
#Ten widok ma adres: /login url.
#Zwraca studentom i nauczycielom stronę do logowania.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            try:
                student = Student.objects.get(user=request.user)
                return redirect('portal:index')
            except:
                return redirect('nauczyciel:nauczyciel_index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'login.html')


#Widok dla strony rejestracji studentów.
#Ten widok ma adres: /register_user url.
#Zwraca formularz rejestracji studenta.
#Studenci wybierają sobie nazwę użytkownika oraz hasło. Podają również pozostałe dane i zapisują się do grup zajęciowych.
def register_user(request):
    user_form = UserRegistration(request.POST or None)
    student_form = StudentRegistration(request.POST or None)

    if user_form.is_valid() and student_form.is_valid():
        user = user_form.save(commit=False)
        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password']
        user.set_password(password)
        user.save()

        student = student_form.save(commit=False)
        student.user = User.objects.get(id=user.id)
        student.save()
        student_form.save_m2m() #Zapisywanie relacji wiele do wielu (między zajęciami a modelem studenta) wprowadzonej w formularzu, podczas wybierania zajęć.

        return login_user(request)

    return render(request,'register_user.html', {'user_form': user_form, 'student_form': student_form})


#Widok dla strony wylogowania.
#Ten widok ma adres: /logout_user url.
#Zwraca stronę logowania, na którą jest przenoszony użytkownik tuż po wylogowaniu.
def logout_user(request):
    logout(request)
    return render(request, 'login.html')

