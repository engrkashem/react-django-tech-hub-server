from django.urls import path
from users.views import UserView
from course.views import CourseView, EnrollView
from job.views import JobView, JobViewID
from blog.views import BlogView, BlogViewID

urlpatterns = [
    path('user/', UserView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('job/', JobView.as_view()),
    path('job/<int:pk>/', JobViewID.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog/<int:pk>', BlogViewID.as_view()),
    path('enroll/', EnrollView.as_view()),
    path('enroll/<int:pk>/', EnrollView.as_view()),

]
