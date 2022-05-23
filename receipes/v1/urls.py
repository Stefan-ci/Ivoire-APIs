from django.urls import path
from receipes.v1 import views



urlpatterns = [
    path('', views.receipes_list_view, name='receipes-list'),
    path('random/', views.random_receipe_view, name='random-receipe'),
    path('random/list/', views.random_receipes_list_view, name='random-receipes-list'),

    path('<int:pk>/', views.receipe_detail_view, name='receipe'),
    path('with-related/<int:pk>/', views.receipe_detail_with_related_view, name='receipe-with-related'),
    path('category/<str:category>/', views.receipes_by_category_list_view, name='receipes-by-category'),

    # path('submit/', views.submit_receipe_view, name='submit-receipe'),


]

