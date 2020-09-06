from django.urls import path 
from Login_App import views

 
app_name = 'Login_App'


urlpatterns = [
    path('sign_up/',views.sign_up, name='sign_up'),
    path('login/',views.login_page,name='login'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('user_profile/<username>/',views.user_profile,name='user_profile'),
    path('follow/<username>/',views.follow,name='follow'),
    path('unfollow/<username>/',views.unfollow,name='unfollow'),


    
]
   