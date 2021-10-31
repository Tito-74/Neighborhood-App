from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url('register/',views.register, name = 'register'),
    url('login/',views.loginPage, name = 'login'),
    url('profile/',views.my_profile, name = 'profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)