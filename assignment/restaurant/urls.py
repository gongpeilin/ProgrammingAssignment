from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    # path('book/', views.book, name="book"),
    path('book2/', views.BookCreateView.as_view(), name="book2"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.display_menu_item, name="menu_item"),
    # path('menu/success/',views.success, name='success'),
    # path('menu/success2/',views.success2, name='success2'),
    
    path('book/success/',views.success, name='success'),
    path('book/<int:pk>/update/',views.BookUpdateView.as_view(), name='edit_booking'),
    path('book/<int:pk>/', views.disaply_booking_item, name="booking_item"),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name="delete_booking"),
    path('book/delete/success/', views.display_booking_Cancelinfo, name="delete_booking_success"),
    # path('menu/success/',views.success, name='success'),
    # Add the remaining URL path configurations here
]