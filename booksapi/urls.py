
from django.urls import path
from . import views

urlpatterns = [
   # path(' ', views.apiOverView, name='apiOverView'),
    path('books-list/', views.ShowAll, name='books-list'),
    path('getdetailbyid/<int:pk>/', views.ViewBooks, name='books-detail'),
    path('addbook/',views.CreateBooks, name='Add-Book'),
    path('updatebyid/<int:pk>/', views.UpdateBooks, name='update-books'),
    path('deletebyid/<int:pk>/', views.DeleteBooks, name='deletete-books'),
    

    
]
