from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    userModelNo = models.CharField(max_length=10)
    userGmail = models.CharField(max_length=500)
    profileName = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.profileName}"