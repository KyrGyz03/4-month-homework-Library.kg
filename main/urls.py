
from django.contrib import admin
from django.urls import path
from book.views import about_me, writers, dateTime


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', about_me),
    path('writers/', writers),
    path('dateTime/', dateTime),

]
