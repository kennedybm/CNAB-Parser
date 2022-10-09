from django.urls import path
from transactions import views

urlpatterns = [
    path("", views.UploadView.as_view(), name="base_url")
]