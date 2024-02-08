
from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('new_page/',views.new_page, name='new_page'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('wikipedia/',views.wikipedia, name='wikipedia'),
]
