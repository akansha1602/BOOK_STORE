from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.index),
    #path("<int:id>",views.book_detail,name="book-detail")
    path("<slug:slug>",views.book_detail,name="book-detail"),
    path("book/",include('api.urls')),

    #path('book/', include('Book.urls')),
    #path('author/', include('Author.urls')),
    #path('address/', include('Address.urls')),
    #path('author/', include('comment.urls')),
]