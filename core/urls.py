from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('desejos/', views.DesejoList.as_view()),
    path('desejos/<int:pk>/', views.DesejoDetail.as_view()),
    path('itens/', views.ItemList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)