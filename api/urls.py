from django.urls import path
from users.views import UserView
from course.views import CourseView
from job.views import JobView
from blog.views import BlogView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('job/', JobView.as_view()),
    path('job/<int:pk>/', JobView.as_view()),
    path('blog/', BlogView.as_view()),
]
