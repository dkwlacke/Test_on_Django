from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls', namespace='main') ),
    path('',include('app1.urls', namespace='calc')),
    path('', include('orm_sql.urls', namespace='sql')),
    path('',include('users.urls',namespace='users'))
]
