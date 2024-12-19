
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('signup/',views.registerForm,name='signup'),
    path('login/',LoginView.as_view(template_name="login.html",next_page='homepage'),name="login"),
    path('logout/',LogoutView.as_view(next_page='homepage'),name="logout"),
    path('post_detail/<int:id>',views.PostDetails.as_view(),name="post_detail"),
    path('buy/<int:id>',views.buy_now,name="buy_now"),
    path('update_profile/',views.change_dat,name="update_profile"),
    path('profile/',views.ProfileVie.as_view(),name="profile"),
    path('searched_item/',views.search_products,name="search_products"),
]