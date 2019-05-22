from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField()

    # This function will in admin page change name of blogs from blog(1) to tittle of that blog
    def __str__(self):
        return self.title

    # This function will create short description of body for blog page
    def summary(self):
        return ' '.join(self.body.split()[:10])

    # we can add new function to costumase date and time using strftime module!
    # i dont want to chage that now :D
