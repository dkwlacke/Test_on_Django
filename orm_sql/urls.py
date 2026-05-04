from django.urls import path
from . import views

app_name = 'sql'
urlpatterns = [
	path('get_db', views.all_db),
	path('find/', views.search)
]