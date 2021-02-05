from django.urls import path
from  .views import Home,DetailPage



urlpatterns = [
    path('', Home.as_view()),
    path('<uuid:pk>/', DetailPage.as_view(),name='detailPage'),
]