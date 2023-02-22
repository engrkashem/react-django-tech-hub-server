from django.urls import path
from users.views import UserView
from course.views import CourseView
from job.views import JobView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('job/', JobView.as_view()),
    path('job/<int:pk>/', JobView.as_view()),
]
