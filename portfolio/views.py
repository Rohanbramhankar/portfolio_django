from django.shortcuts import render
from .models import Project, Profile, Skill, Education, Experience, Service

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-id')[:4] 
    education_list = Education.objects.all().order_by('-id')
    experiences = Experience.objects.all().order_by('-id')
    
    return render(request, 'index.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'project_count': Project.objects.count(),
        'education_list': education_list,
        'experiences': experiences,
        'services': Service.objects.filter(is_visible=True),
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


from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and subject and message:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            try:
                EmailMessage(
                    subject=f"Portfolio Contact: {subject}",
                    body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                    reply_to=[email],
                ).send()
                messages.success(request, "Message sent successfully!")
            except Exception:
                messages.error(request, "Message saved, but the email could not be sent.")
        else:
            messages.error(request, "Please fill in all fields.")
        return redirect('contact')

    return render(request, 'portfolio/contact.html')