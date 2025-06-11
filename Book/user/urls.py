from django.urls import path 
from .views import Register,user_login,user_logout,user_profile,update_profile_picture
urlpatterns = [
    path('',Register,name='register'),
    path('logout',user_logout,name='logout'),
    path('login',user_login,name='login'),
    path('profile',user_profile,name="profile"),
    path('update-profile-pic/',update_profile_picture, name='update_profile_pic'),
    
]
