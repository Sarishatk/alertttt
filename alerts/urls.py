from django.urls import path
from . import views

urlpatterns = [
    path("", views.records, name="records"),
    path("add/", views.add_alert, name="add_alert"),
    path("edit/<int:pk>/", views.edit_alert, name="edit_alert"),
    path("delete/<int:pk>/", views.delete_alert, name="delete_alert"),
]
