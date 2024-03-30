from django.urls import path

from . import views

app_name = 'tfidf'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('mainlist/', views.MainListView.as_view(), name='main_list'),
    path('documentcreate/', views.DocumentAddView.as_view(), name='document_create'),
]
