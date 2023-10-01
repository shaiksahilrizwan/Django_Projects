from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header="ToDos Administration"
admin.site.site_title="Here is your DashBoard Master "
admin.site.index_title="Welcome Web Master"
urlpatterns = [
    
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('task',views.task,name="task")
    
]
