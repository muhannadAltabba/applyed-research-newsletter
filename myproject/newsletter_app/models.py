from django.db import models
from django.core.validators import RegexValidator
from phone_field import PhoneField
from datetime import datetime   
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class Domain(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ='domain')
    description = models.CharField(max_length=150, default='')
    def __str__(self):
        return self.name 


class Section(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Contributor(models.Model):
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^09[0-9]{8}$', message="Phone number must be start with: '09'")
    phone = models.CharField(validators=[phone_regex], blank=True, unique=True, max_length=10)  # Validators should be a list
    email = models.EmailField(unique=True)
    photo =  models.ImageField(upload_to ='contributor', default='contributor/empty.jpg')
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    sharepoint = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    abstruct_problem = models.TextField()
    abstruct_contribution = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    contributor = models.ManyToManyField(Contributor)
    publisher = models.ManyToManyField(Publisher)
    # publication_date = models.DateTimeField(default=datetime.now())
    publication_date = models.PositiveIntegerField(validators=[MinValueValidator(1984), MaxValueValidator(datetime.today().year)])
    views = models.IntegerField(default=0, editable=False)
    lead = models.ImageField(upload_to ='article/image')
    article_file =  models.FileField(upload_to ='article/file')
    
    class Meta:
        ordering = ('-created_at',)

    def contributor_name(self):
        return "\n".join([c.name for c in self.contributor.all()])


