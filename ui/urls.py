from django.urls import path

from ui.views import user, dashboard, menu

urlpatterns = [
    path('', dashboard.dashboard, name='dashboard'),
    path('login', user.login_view, name="login"),
    path('logout', user.logout_view, name="logout"),
    path('menu', menu.main_page, name="menu"),
    path('menu/read', menu.read_menu, name="read_menu"),
    path('menu/save', menu.save_menu, name="save_menu"),
    path('menu/delete', menu.delete_menu, name="delete_menu"),
    path('menu/categories', menu.read_categories, name="read_categories"),
    path('menu/categories/save', menu.save_category, name="save_category"),
    path('menu/categories/delete', menu.delete_category, name="delete_category"),
]
