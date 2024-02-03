from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.end, name = 'end'),
    path('body/', views.body, name = 'body' ),
    path('home/',views.home, name = 'home'),
    path('timeline/',views.timeline, name = 'timeline'),
    path('about/',views.about, name = 'about'),
    path('feedback/',views.feedback, name = 'feedback'),
    path('contact/',views.contact, name = 'contact')
]