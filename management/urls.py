from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('proposal/detail/<int:pk>/', views.ProposalDetailView, name='detail'),
    path('proposal/edit/<int:pk>', views.edit, name='edit'),
    path('proposal/new', views.proposalview, name='proposal'),
    path('proposal/delete/<int:pk>', views.delete, name='delete'),
]