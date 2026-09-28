from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python Projects'),
        
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text="Enter GitHub Repository URL")
    created_at = models.DateTimeField(auto_now_add=True)
    technology = models.CharField(max_length=200, default="Python, Django")
    project_file = models.FileField(upload_to='project_files/', blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    hero_description = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.full_name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Languages'),
        ('framework', 'Web Frameworks & Libraries'),
        ('ai_data', 'AI & Data Science'),
        ('tool', 'Tools'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"


class Education(models.Model):
    degree = models.CharField(max_length=200) # B.Tech in Computer Science
    institution = models.CharField(max_length=200) #  GH Raisoni University
    duration = models.CharField(max_length=100) #  2023 – 2027
    description = models.TextField(blank=True, null=True) # Relevant Coursework: DSA...

    def __str__(self):
        return self.degree



class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)  # e.g., Python Developer Intern
    duration = models.CharField(max_length=100)  # e.g., June 2023 – August 2023
    description = models.TextField(help_text="Describe your responsibilities and achievements")
    is_internship = models.BooleanField(default=True)  # True for Internship, False for Job

    def __str__(self):
        return f"{self.role} at {self.company}"


class Service(models.Model):
    ICON_CHOICES = [
        ('fa-code', 'Code'),
        ('fa-server', 'Backend / Server'),
        ('fa-globe', 'Web'),
        ('fa-mobile-screen', 'Mobile'),
        ('fa-chart-column', 'Data / Charts'),
        ('fa-database', 'Database'),
        ('fa-microchip', 'AI / Chip'),
        ('fa-robot', 'Robot / Agents'),
        ('fa-gears', 'Automation'),
        ('fa-cloud', 'Cloud'),
        ('fa-shield-halved', 'Security'),
        ('fa-palette', 'Design'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(help_text="1-2 short lines")
    icon = models.CharField(max_length=40, choices=ICON_CHOICES, default='fa-code')
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


