from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


        def  save(self):
            super().save()

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=50)

