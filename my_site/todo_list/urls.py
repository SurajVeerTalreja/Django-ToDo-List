from django.urls import path
from .views import index, TodoCreateView, all_items, item_detail, delete_item

urlpatterns = [
    path('', index, name='home-page'),
    path('create_activity/', TodoCreateView.as_view(), name='create-item'),
    path('all-items/', all_items, name='all-items'),
    path('item_detail/<slug:slug>', item_detail, name='item-detail'),
    path('delete_item/<slug:slug>', delete_item, name='delete-item'),
]
