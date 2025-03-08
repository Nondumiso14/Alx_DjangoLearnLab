from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author =  models.CharField(max_length=100)
    publication_year = models.IntegerField

from django.contrib.auth.models import AbstractUser, BaseUserManager
class CustomUserManager(BaseUserManager):
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
    class CustomUser(AbstractUser):
        email = models.EmailField(unique=True, max_length=256)
        username = models.UsernameField(unique=False, max_length=100)
        date_of_birth = models.DateField(unique=False, max_length=100)
        profile_photo = models.ImageField

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
