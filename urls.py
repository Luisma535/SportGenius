<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talentos/', include('talentos.urls')),
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talentos/', include('talentos.urls')),
>>>>>>> 1e9d24980816ceb6a1f657cd2570d9f46983f0ad
]