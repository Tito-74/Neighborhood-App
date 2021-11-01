from django.conf.urls import url
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url('register/',views.register, name = 'register'),
    url('login/',views.loginPage, name = 'login'),
    url('profile/',views.my_profile, name = 'profile'),
    path('update/<id>',views.update_profilePage, name = 'update_profile'),
    url('add/',views.eventPost, name = 'add'),
    url('event/(?P<id>\d+)/', views.viewEvents, name='event'),
    url('buzpost/',views.addBuzpost, name = 'business_post'),
    path('business/',views.businessView, name = 'business'),
    path('Neighbourhood/',views.addNeighbourhood, name = 'neighbourhood'),
    url(r'^search/', views.search, name='search'),

   

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)