from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    '''
    Renders a summernote rich text editor for the content of the admin page
    in the admin area.
    '''
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    '''
    Displays a list of collaboration messages in the admin area
    with the message and read fields.
    '''
    list_display = ('message', 'read',)
