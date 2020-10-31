from django.urls import path

from . import views


urlpatterns = [
    path('passport/', views.PassportView.as_view()),
    path('add_passport/', views.PassportView.as_view()),
    path('document/', views.DocumentView.as_view()),
    path('add_document/', views.DocumentView.as_view()),
    path('qualification/', views.QualificationView.as_view()),
    path('qualification/rules/', views.QualificationRulesView.as_view()),
    path('qualification/accept/', views.QualificationAcceptView.as_view()),
]