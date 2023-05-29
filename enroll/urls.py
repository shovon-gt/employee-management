from django.urls import path

from . import views

urlpatterns = [
     path('', views.user_login, name='login'),
    path('add-show', views.add_show, name="add-show"),
    path('add-employee', views.add_employee, name="add-employee"),
    path('delete/<int:id>', views.delete_data, name="delete-data"),
    path('<int:id>', views.update_data, name="update-data"),

]
