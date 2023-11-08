from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    author=models.CharField(null=True,max_length=100)
    is_bestselling=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[self.id])
    
















""" step 1- create dbsqllite3 file and create class
    step2- update installed apps in settings.py with book_outlet
    step3- create migartions- terminal: python3 manage.py makemigrations
    step4- go to terminal and type python3 manage.py migrate to have a look and run all migrations
    step 5- SAVING DATA:run commands: python3 manage.py shell
    from book_outlet.models import Book
    harry_potter=Book(title="Harry Potter-The Philosopher's Stone",rating=5),
    harry_potter.save() to save entry in database, and add more entries.
    step6-GETTING DATA:Book.objects.all()
    step 7-  go to models.py and override __str__() method to set how objects rendered in console
    step 8- add validators to ratings, new fields and to update the databse, run python3 manage.py
    makemigrations in shell.(ALL MIGRATIONS ARE RUN ON TERMINAL NOT SHELL) ,  GETTING  DATA IS DONE ON SHELL
    step 9-UPDATE DATA( through shell):harry_potter=Book.objects.all()[0]
    harry_potter.author="J.K Rowling, harry_potter.save()
    step9- DELETE:harry_potter=Book.objects.all()[0],harry_potter.delete()
    step 10-CREATE:new onjects can be directly created using create command:
    Book.objects.create(title="LOTR",rating=5,author="unknown")
    step 11- quering and filtering- Book.objects.get(id=1) or use title="" inplace of id
    for multiple resuls use filter:Book.objects.filter(is_bestselling=False,rating__lte=5)
    step 12- AND- use , for OR conditions - from django.db.models import  Q  ,Book.objects.filter(Q(rating__lt=3)|Q(is_bestselling=True))
    step 13-prepare templates: add templates in book_outlet, and aad book.detail.html and other files 
    in the book_outlet folder in templates. Now go to views.py and write index function, add urls.py in book_outlet app
    and write urlpatterns .
    step 14-In the project urls file include the added urls file.
    step 15-modify index function in views to get data.
    step 16- work on book_detail page and add the corrasponding view in views.py, add it in urlspatterns
    step 17- wire up index and book_detail pages by adding links. By adding name to path in urlpatterns
    step 18-(did not implement-slug) make and run migrations






      """