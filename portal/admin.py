from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Student, Message, Notification, Resources, Topic, Entry


class EntryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# Register your models here.

admin.site.register(Student)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Resources)
admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
