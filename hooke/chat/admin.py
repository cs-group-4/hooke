from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Message, Inbox
# Register your models here.



class MessageAdmin(ModelAdmin):
    list_display = ['sender', 'receiver']



class InboxAdmin(ModelAdmin):
    list_display = ['name']
    readonly_fields = ['name']


admin.site.register(Message,MessageAdmin)
admin.site.register(Inbox,InboxAdmin)