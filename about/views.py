from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here.
def about_me(request):
    '''
    Renders the most recent information on the website author 
    and allows collaboration requests
    Displays an individual instance of :model:`about.About`.
    **Context**
    ``about``
        The most recent instance of :model:`about.About`
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`
    **Template**
    :template:`about/about.html`
    '''
    about = About.objects.all().order_by('-updated_on').first()

    collaborate_form = CollaborateForm()

    if request.method == "POST":
        print("Received the POST request")
        collaborate_form = CollaborateForm(data=request.POST)
    if collaborate_form.is_valid():
        collaborate_form.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Collaboration request received! '
            + 'I endeavour to respond within 2 working days.'
        )

    return render(
        request,
        "about/about.html",
        {"about": about,
            "collaborate_form": collaborate_form},
    )
