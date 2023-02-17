from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.product_list, name='home'),
    path('index/', views.index, name='index'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('category/<int:category_id>/carousel/', views.category_carousel, name='category_carousel'),
]
