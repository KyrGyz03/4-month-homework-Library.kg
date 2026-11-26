
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from book.views import about_me, writers, dateTime, book_list, book_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list),
    path('books/<int:id>/', book_detail),
    path('about_me/', about_me),
    path('writers/', writers),
    path('dateTime/', dateTime),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
