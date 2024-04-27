from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]