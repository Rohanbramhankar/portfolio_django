from django.shortcuts import render
from .models import Project, Profile, Skill, Education

from .models import Profile, Skill, Project
def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-id')[:2] 
    education_list = Education.objects.all().order_by('-id')
    
    return render(request, 'index.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'education_list': education_list
    })


def contact(request):
    return render(request, 'portfolio/contact.html')

def python_projects(request):
    projects = Project.objects.all().order_by('-created_at') 
    return render(request, 'python_projects.html', {'projects': projects})

def data_analytics_projects(request):
    return render(request, 'data_analytics_project.html')
def dotnet_projects(request):
    return render(request, 'dotnet_projects.html')


from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

def contact(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            f"Portfolio Contact: {subject}",
            f"""
Name: {name}
Email: {email}

Message:
{message}
            """,
            email,
            ['rohanbramhankar@gmail.com'],
            fail_silently=False,
        )

        # Success Message
        messages.success(
            request,
            "Message sent successfully!"
        )

        return redirect('contact')

    return render(request, 'portfolio/contact.html')