# from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('forecast/', include('forecast.urls')),
    # path('admin/', admin.site.urls),
]
