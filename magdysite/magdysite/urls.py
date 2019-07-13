
from django.contrib import admin
from django.urls import path
from newapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',v.index),

]
urlpatterns+=staticfiles_urlpatterns()
