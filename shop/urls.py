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
    path('<int:id>/<slug:slug>/review/',
         views.review_product, name='review_product'),
    path('<int:product_id>/<slug:product_slug>/review/<int:review_id>/edit/',
         views.edit_review, name='edit_review'),
    path('category/<int:category_id>/carousel/',
         views.category_carousel, name='category_carousel'),
    path('<int:product_id>/<slug:product_slug>/reviews/<int:review_id>/delete/',
         views.delete_review, name='delete_review'),
]
