from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.QuestionList.as_view(), name="get_questions"),
    path('question/add', views.QuestionCreate.as_view(), name='create_question'),
    path('question/find/<int:pk>/', views.QuestionDetail.as_view(), name='detail'),
    path('question/update/<int:pk>/', views.QuestionUpdate.as_view(), name='update_question'),
    path('question/delete/<int:pk>/', views.QuestionDelete.as_view(), name='delete_question'),
]
