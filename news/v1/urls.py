from news.v1 import views
from django.urls import path





urlpatterns = [
    path('', views.articles_list_view, name='articles-list'),
    path('random/', views.random_article_view, name='random-article'),
    path('random/list/', views.random_articles_list_view, name='random-articles-list'),

    path('search/', views.search_articles_view, name='search-articles'),

    path('<int:pk>/', views.article_detail_view, name='article'),
    path('with-related/<int:pk>/', views.article_detail_with_related_view, name='article-with-related'),
    path('category/<str:category>/', views.articles_by_category_list_view, name='articles-by-category'),

    path('submit/', views.submit_article_view, name='submit-article'),


]


