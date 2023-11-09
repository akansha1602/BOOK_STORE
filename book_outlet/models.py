from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=80)
    code=models.CharField(max_length=2)

    class Meta:
        verbose_name_plural="Countries"
        #if there are multiple contries this is displayed/output instead of "contrys"




class Address(models.Model):
    street=models.CharField(max_length=80)
    postal_code=models.CharField(max_length=5)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street, {self.postal_code},{self.city}}"
    class Meta:
        verbose_name_plural="Address Entries"
        #if there are multiple addresses this is displayed/output instead of "address"

    

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address=models.OneToOneField(Address, on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    #author=models.CharField(null=True,max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=True,null=False)
    published_countries=models.ManyToManyField(Country)


    """ to add slugs this function has to be overridden"""
    """def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)#to save data to db"""

    
    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[str(self.slug)])
    
















""" INITIAL SETUP WITH ONLY ONE MODEL
step 1- create dbsqllite3 file and create class Book
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
    makemigrations.(ALL MIGRATIONS ARE RUN ON TERMINAL NOT SHELL) ,  GETTING  DATA IS DONE ON SHELL
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
    step 19-Change urls.py to have slug instead of id and views.py book_detail function, get_absolute url replace id by slug
    call the save() methods on the objects to add slug.
    step 20-ADMINS: create superuser to login to admin,use in terminal
    python3 manage.py createsuperuser, create password runserver and go to localhost:8000/admin/
    and login
    step 21- go to admins.py and register models there,reload and see book_outlet shows up there
    add new Books
    step 22- customize admin.py to prepopulate w required fields etc. Once admin.py is written, remove the save method in models.py
    add list filter to BookAdmin
"""

""" WORKING WITH MULTIPLE MODELS
    (one to one many)
   step 1- Add class author.Add author as fk in class book, run makemigrations .
   step2- Clear all book data from shell and run migrations.
   
   step3- ADD authors and books:
    from book_outlet.models import Book
>>> from book_outlet.models import Book,Author
>>> jk=Author(first_name="J.K",last_name="Rowling")
>>> jk.save()
    Author.objects.all()
>>> hp1=Book(title="Harry Potter 1",rating=5,is_bestselling=True,slug="harry-potter-1",author=jk)
>>> hp1.save()
>>> Book.objects.all()
>>> harry=Book.objects.get(title="Harry Potter 1")
    harry.author
>>> harry.author.first_name
'J.K'
    step 4- CROSS MODEL QUERING
    
    1)GET AUTHOR INFO FROM BOOK
>>> RowlingBooks=Book.objects.filter(author__last_name="Rowling") 
>>> RowlingBooks
<QuerySet [<Book: Harry Potter 1 (5)>]>
>>> RowlingBooks=Book.objects.filter(author__last_name__contains="wling")
>>> RowlingBooks
<QuerySet [<Book: Harry Potter 1 (5)>]>
    
    2)GET BOOK INFO FROM AUTHOR
>>> jkr=Author.objects.get(first_name="J.K")
>>> jkr.book_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x109e353d0>
>>> jkr.book_set.all()
<QuerySet [<Book: Harry Potter 1 (5)>]>
can put related_name="nameOfChoice" in fk field to replace book_set by desired name, makemigrations and  migrate.
>>> from book_outlet.models import Book, Author
>>> jkr=Author.objects.get(first_name="J.K")
>>> jkr.books.all()
<QuerySet [<Book: Harry Potter 1 (5)>]>
>>> jkr.books.get(title="Harry Potter 1")
<Book: Harry Potter 1 (5)>

step 5- ADD MODELS TO ADMINISTRATIVE AREA
import author to admins.py ,register it ,runserver and reload admin page
chane how objects are displayed in the admin page by overridibg __str__,
explore relations in admin interface.

step 6- ADD ONE TO ONE MODEL
add address class.
add address field in author and create one to one relation,make migrations and migrate.
step 7- GET INFO FROM AUTHOR AND ADDRESS

>>> from book_outlet.models import Author,Address,Book
>>> Author.objects.all()
<QuerySet [<Author: J.K Rowling>]>
>>> addr1=Address(street="somestreet",postal_code="6789",city="NY")
>>> addr2=Address(street="somestreet",postal_code="1234",city="London")
>>> addr1.save()
>>> addr2.save()
>>> jkr=Author.objects.get(first_name="J.K")
>>> jkr.address=addr1
>>> jkr.save()
>>> jkr.address.street
'somestreet'
>>> Address.objects.all()[0].author
<Author: J.K Rowling>

step 8- register Address on admins page ,runserver and go to admins page,override string to set what do
display in admin page.
step 9- add the nested class Meta for further customization of properties in address

step 10-ADDING MANY TO MANY RELATION
add country class,set up  manytomany relations in book class(NO ONDELETE CASCADE).
run commands in sheell and then check admin page to see relations:
>>> from book_outlet.models import Country,Book
>>> germany=Country(name="Germany",code="DE")
>>> mys=Book.objects.all()[0]
>>> germany.save()
>>> mys.published_countries.add(germany)
>>> mys.published_countries.filter(code="DE")
<QuerySet [<Country: Country object (1)>]>
OTHER WAY ROUND
ger= Country.objects.all()[0]
>>> ger.book_set.all()
<QuerySet [<Book: Harry Potter 1 (5)>]>
step 11- Register country in admin and explore that page
add meta class, makemigrations runmigrations, can override str as well



"""