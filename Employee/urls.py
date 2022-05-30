from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListCreateAPIView.as_view()),
    path('<int:pk>/', views.EmployeeRetrieveUpdateDeleteAPIView.as_view()),
]
