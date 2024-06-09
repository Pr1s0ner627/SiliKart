from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('about/', views.about ,name='about'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('editUser/', views.editUser, name='editUser'),
    path('editPassword/', views.editPassword, name='editPassword'),
    path('product/<int:pk>', views.product, name='product'),
    path('categories/<str:cat>', views.category, name='category'),
    path('categorySummary/', views.categorySummary, name='categorySummary')
]