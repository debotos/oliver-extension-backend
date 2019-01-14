from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Screenseal Admin"
admin.site.site_title = "Screenseal Admin Portal"
admin.site.index_title = "Welcome to Screenseal Admin Portal"

urlpatterns = [
    path('', admin.site.urls),
    # path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
]
