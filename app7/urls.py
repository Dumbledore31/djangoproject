from django.urls import path
from . import views
app_name="app7"
urlpatterns=[
    path('hello',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('show_users',views.show_users,name='show_users'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),
    path('gallery',views.gallery,name='gallery'),
    path('display',views.display,name='display'),
] 