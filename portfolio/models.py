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
    degree = models.CharField(max_length=200) # उदा. B.Tech in Computer Science
    institution = models.CharField(max_length=200) # उदा. GH Raisoni University
    duration = models.CharField(max_length=100) # उदा. 2023 – 2027
    description = models.TextField(blank=True, null=True) # उदा. Relevant Coursework: DSA...

    def __str__(self):
        return self.degree
