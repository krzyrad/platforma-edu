#Widoki dla aplikacji portal.

from django.contrib.auth.decorators import login_required
from .models import Student, Message, Notification, Resources, Topic, Entry
from nauczyciel.models import Assignment, Course, Instructor
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .forms import MessageForm, SubmissionForm, TopicForm, EntryForm
import datetime

# Create your views here.

#Widok dla strony głównej studenta.
#Ten widok ma adres: /index url.
#Zwraca stronę domową studenta, zawierającą wszystkie zajęcia i powiadomienia.
@login_required
def index(request):
    student = Student.objects.get(user=request.user)
    courses = student.portal_list.all()
    notifications = Notification.objects.filter(portal__in=courses)
    return render(request, 'portal/index.html', {'courses': courses, 'notifications': notifications})

#Widok dla strony tematów notatek.
#Ten widok ma adres /topics url.
#Zwraca stronę zawierającą listę wszystkich tematów notatek.
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'portal/topics.html', context)

#Widok dla strony tematu.
#Ten widok ma adres: /topic url.
#Zwraca stronę zawierającą temat i powiązane z nim notatki.
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    #Upewniam się, że temat należy do bieżącego użytkownika
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'portal/topic.html', context)

#Widok dla strony dodawania nowego tematu.
#Ten widok ma adres: new_topic url.
#Zwraca stronę zawierającą formularz dodawania nowego tematu notatki.
@login_required
def new_topic(request):
    if request.method != 'POST':
        #Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = TopicForm()
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('portal:topics'))

    context = {'form': form}
    return render(request, 'portal/new_topic.html', context)

#Widok dla strony dodawania nowej notatki.
#Ten widok ma adres: new_entry url.
#Zwraca stronę zawierającą formularz dodawania nowej notatki.
@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #Nie przekazano żadnych danych, nalezy utworzyć pusty formularz.
        form = EntryForm()
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('portal:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'portal/new_entry.html', context)
#Widok dla strony edycji notatki.
#Ten widok ma adres: edit_entry url.
#Zwraca stronę zawierającą formularz edycji notatki.
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #Żądanie początkowe, wypełnienie formularza aktualną treścią wpisu.
        form = EntryForm(instance=entry)
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portal:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'portal/edit_entry.html', context)

#Widok dla strony zawierającej grupowe forum oraz odnośniki do zadań i dodatkowych zasobów.
#Ten widok ma adres: /detail url.
#Zwraca stronę zawierającą forum oraz łącza do listy zadań i dodatkowych zasobów.
@login_required
def detail(request, portal_id):
    user = request.user
    student = Student.objects.get(user=request.user)
    courses = student.portal_list.all()
    portal = Course.objects.get(id=portal_id)
    nauczyciel = portal.nauczyciel
    messages = Message.objects.filter(portal=portal)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.portal = portal
            message.sender = user
            message.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y') #Zdobądź aktualną datę i przekonwertuj ją na ciąg znaków.
            message.save()
            try:
                student = Student.objects.get(user=request.user)
                return redirect('portal:detail', portal_id)

            except:
                return redirect('nauczyciel:nauczyciel_detail', portal.id)

    else:
        form = MessageForm()

        context = {
            'portal': portal,
            'user': user,
            'nauczyciel': nauczyciel,
            'student': student,
            'courses': courses,
            'messages': messages,
            'form': form
        }

        return render(request, 'portal/detail.html', context)


#Widok dla strony zawierającej listę zadań.
#Ten widok ma adres: /view_assignments url.
#Zwraca stronę zawierającą zadania oraz łącza do ich pobrania i wysłania rozwiązania.
@login_required
def view_assignments(request, portal_id):
    portal = Course.objects.get(id=portal_id)
    assignments = Assignment.objects.filter(portal=portal)
    context = {
        'portal' : portal,
        'assignments' : assignments,
    }
    return render(request,'portal/view_assignments.html',context)


#Widok dla strony zawierającej dodatkowe zasoby.
#Ten widok ma adres: /view_resources url.
#Zwraca stronę zawierającą wszystkie dodatkowe zasoby oraz łącza do ich pobrania.
@login_required
def view_resources(request, portal_id):
    portal = Course.objects.get(id=portal_id)
    resources = Resources.objects.filter(portal=portal)
    context = {
        'portal' : portal,
        'resources' : resources,
    }
    return render(request,'portal/view_resources.html',context)


#Widok dla strony pozwalającej na przesyłanie rozwiązanych zadań.
#Ten widok ma adres: /upload_submission url.
#Zwraca stronę zawierającą formularz wysyłania rozwiązań do zadań i przenosi z powrotem do strony zawierającej listę zadań.
@login_required
def upload_submission(request, assignment_id):
    form = SubmissionForm(request.POST or None, request.FILES or None)
    assignment = Assignment.objects.get(id=assignment_id)
    portal_id = assignment.portal.id
    portal = Course.objects.get(id=portal_id)
    if form.is_valid():
        submission = form.save(commit=False)
        submission.user = request.user
        submission.assignment = assignment
        submission.time_submitted = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        submission.save()
        return view_assignments(request, portal_id)

    return render(request, 'portal/upload_submission.html', {'form': form,'portal': portal})
