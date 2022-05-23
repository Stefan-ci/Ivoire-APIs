from core import views
from django.urls import path



urlpatterns = [
    path('', views.home_view, name='home'),

    path('docs/', views.apis_documentations_view, name='api-docs'),
    path('docs/<str:version>/', views.api_documentation_view, name='api-doc'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile_view, name='profile'),

]


