from django.urls import path

from .views import HomePageView,PostDetailView,PostFormView
app_name = 'feed'
urlpatterns=[
    path('',HomePageView.as_view(),name='index'),
    path('info/<int:pk>/',PostDetailView.as_view(),name="detail"),
    path('post/',PostFormView.as_view(),name='post')
]


    
