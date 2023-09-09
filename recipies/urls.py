from django.urls import path
from . import views
urlpatterns = [
    path('add_recipy/',views.create_recipy,name="add_recipy"),
    path('recipy_profile/',views.recipy_profile,name="recipy"),
    path('update_profile/<int:pk>/',views.update_recipy.as_view(),name="updatepage"),
    path('searched/',views.search_recipy,name="searchfood"),
    path('blogs/<slug:category_slug>/',views.blog_view,name="blogs"),   
    path('blogs/',views.blog_view,name="blogs"),   
]