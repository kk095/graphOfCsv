from django.urls import path
from .views import Home,Chart,Signup,Logout,Login,Newpass,Newpassdone,Circle

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('chart', Chart.as_view(),name='chart'),
    path('signup', Signup.as_view(),name='signup'),
    path('logout', Logout.as_view(),name='logout'),
    path('login', Login.as_view(),name='login'),
    path('newpass', Newpass.as_view(),name='newpass'),
    path('newpassdone', Newpassdone.as_view(),name='Newpassdone'),
    path('anim', Circle.as_view(),name='circle'),
]