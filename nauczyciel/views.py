#Widoki dla aplikacji nauczyciel.

from django.contrib.auth.decorators import login_required
from .models import Instructor, Submission, Assignment
from portal.models import Course, Message, Notification, Student
from django.shortcuts import render, HttpResponse, redirect
from .forms import AssignmentForm, NotificationForm, ResourceForm
from portal.forms import MessageForm
import datetime


#Widok dla strony głównej nauczyciela.
#Ten widok ma adres: /nauczyciel_index url.
#Zwraca stronę główną nauczyciela, zawierającą łącza do prowadzonych przez niego zajęć.
@login_required
def nauczyciel_index(request):
    user = request.user
    nauczyciel = Instructor.objects.get(user=request.user)
    courses = Course.objects.filter(nauczyciel=nauczyciel)
    context = {
        'user': user,
        'nauczyciel': nauczyciel,
        'courses': courses,
    }
    return render(request, 'nauczyciel/nauczyciel_index.html', context)


#Widok dla strony głównej grupy zajęciowej.
#Ten widok ma adres: /nauczyciel_detail url.
#Zwraca stronę grupy zajęciowej, zawierającą forum dyskusyjne oraz odnośniki do zadań, rozwiązań, dodatkowych zasobów i ogłoszeń.
@login_required
def nauczyciel_detail(request, portal_id):
    user = request.user
    nauczyciel = Instructor.objects.get(user=request.user)
    courses = Course.objects.filter(nauczyciel=nauczyciel)
    portal = Course.objects.get(id=portal_id)
    messages = Message.objects.filter(portal=portal)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.portal = portal
            message.sender = user
            message.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
            message.save()
            try:
                student = Student.objects.get(user=request.user)
                return redirect('portal:detail', portal_id)

            except:
                return redirect('nauczyciel:nauczyciel_detail', portal.id)

    else:
        form = MessageForm()

        context = {
                'user': user,
                'nauczyciel': nauczyciel,
                'portal': portal,
                'courses': courses,
                'messages': messages,
                'form' : form
            }

        return render(request, 'nauczyciel/nauczyciel_detail.html', context)


#Widok dla strony dodawania ogłoszenia.
#Ten widok ma adres: /add_notification url.
#Zwraca stronę zawierającą formularz dodawania ogłoszenia. Po dodaniu ogłoszenia, automatycznie przenosi do strony głównej grupy zajęciowej.
@login_required
def add_notification(request, portal_id):
    form = NotificationForm(request.POST or None)
    portal = Course.objects.get(id=portal_id)
    if form.is_valid():
        notification = form.save(commit=False)
        notification.portal = portal
        notification.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y') #pobierz aktualną datę i godzinę, a nastepnie zamień na ciąg znaków
        notification.save()
        return redirect('nauczyciel:nauczyciel_detail', portal.id)

    return render(request, 'nauczyciel/add_notification.html', {'portal': portal, 'form': form})


#Widok dla strony dodawania zadania.
#Ten widok ma adres:/add_assignment url.
#Zwraca stronę zawierającą formularz dodawania zadania. Po dodaniu zadania, przenosi do strony głównej grupy zajęciowej.
@login_required
def add_assignment(request, portal_id):
    form = AssignmentForm(request.POST or None, request.FILES or None)
    portal = Course.objects.get(id=portal_id)
    if form.is_valid():
        assignment = form.save(commit=False)
        assignment.file = request.FILES['file']
        assignment.post_time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        assignment.portal = portal
        assignment.save()
        notification = Notification()
        notification.content = "Zamieszczono nowe zadanie"
        notification.portal = portal
        notification.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        notification.save()
        return redirect('nauczyciel:nauczyciel_detail', portal.id)

    return render(request, 'nauczyciel/create_assignment.html', {'form': form, 'portal': portal})


#Widok dla strony dodwania dodatkowych zasobów.
#Ten widok ma adres:/add_resource url.
#Zwraca stronę zawierającą formularz wysyłania dodatkowych zasobów. Po dodaniu dodatkowych zasobów, przenosi do strony głównej grupy zajęciowej.
@login_required
def add_resource(request, portal_id):
    form = ResourceForm(request.POST or None, request.FILES or None)
    nauczyciel = Instructor.objects.get(user=request.user)
    portal = Course.objects.get(id=portal_id)
    if form.is_valid():
        resource = form.save(commit=False)
        resource.file_resource = request.FILES['file_resource']
        resource.portal = portal
        resource.save()
        notification = Notification()
        notification.content = "Zamieszczono nowe zasoby"
        notification.portal = portal
        notification.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        notification.save()
        return redirect('nauczyciel:nauczyciel_detail', portal.id)

    return render(request, 'nauczyciel/add_resource.html', {'form': form, 'portal': portal})


#Widok dla strony wyświetlającej dodane zadania.
#Ten widok ma adres: /view_all_assignments url.
#Zwraca stronę zawierającą listę wszystkich zadań i łącza przenoszące listy zawierającej przesłane rozwiązania.
@login_required
def view_all_assignments(request, portal_id):
    portal = Course.objects.get(id=portal_id)
    assignments = Assignment.objects.filter(portal=portal)
    return render(request, 'nauczyciel/view_all_assignments.html', {'assignments' : assignments,'portal': portal})


#Widok dla strony wyświetlającej listę studentów i przesłanych przez nich rozwiązań.
#Ten widok ma adres: /view_all_submissions url.
#Zwraca stronę zawierającą listę przesłanych przez studentów rozwiązań do zadania.
@login_required
def view_all_submissions(request,assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    submissions = Submission.objects.filter(assignment=assignment)
    portal = assignment.portal
    return render(request, 'nauczyciel/view_all_submissions.html', {'submissions' : submissions,'portal': portal})

