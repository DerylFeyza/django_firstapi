from django.urls import path
from . import views

urlpatterns = [
    path('question', views.question_list, name="get_questions"),
    path('question/add', views.question_create, name='create_question'),
    path('question/find/<int:pk>', views.question_detail, name='detail'),
    path('question/update/<int:pk>', views.question_update, name='update_question'),
    path('question/delete/<int:pk>', views.question_delete, name='delete_question'),
]
