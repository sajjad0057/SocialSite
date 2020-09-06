from django.urls import path
from Posts_App import views

app_name = 'Posts_App'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('like/<pk>/',views.like,name='like'),
    path('unlike/<pk>/',views.unlike,name='unlike'),
    path('update_post/<pk>/',views.update_post,name='update_post'),
    path('delete_post/<pk>/',views.delete_post,name='delete_post'),
]