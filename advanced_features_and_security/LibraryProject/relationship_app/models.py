from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
            permissions = [
                ("can_add_book", "Can add book"),
                ("can_change_book", "Can change book"),
                ("can_delete_book", "Can delete book"),
            ]

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Librian_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

from django.contrib.auth.models import AbstractUser, BaseUserManager
Class CustomerUser(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email required")
    
    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)

    return user

    def create_superuser(self, email, password=None):
    user = self.create_user(email, password)

    user.is_staff = True
    user.is_superuser = True
    user.save(using=self.db)
    
    return user
    
Class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=256)
    username = models.UsernameField(unique=False, max_length=100)
    date_of_birth = models.DateField(unique=False, max_length=100)
    profile_photo = models.ImageField

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    