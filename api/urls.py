from django.urls import path
from users.views import UserView
from course.views import CourseView, EnrollView, EnrollUserView
from job.views import JobView, JobViewID, ApplicationView

from blog.views import BlogView, BlogViewID
from payment.views import StripePaymentView, SaveStripeInfo

urlpatterns = [
        path('payment/stripe-test-payment/', StripePaymentView.as_view()),
    path('payment/save-stripe-info/', SaveStripeInfo.as_view()),
    path('user/', UserView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('job/', JobView.as_view()),
    path('job/<int:pk>/', JobViewID.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog/<int:pk>', BlogViewID.as_view()),
    path('enroll/', EnrollView.as_view()),
    path('enroll/<int:pk>/', EnrollView.as_view()),
    path('application/', ApplicationView.as_view()),
    path('application/<int:pk>/', ApplicationView.as_view()),
    # path('enrolluser/<int:pk>/', Enrolluser.as_view()),
    path('enrollments/user/<int:user_id>/',EnrollUserView.as_view(), name='user-enrollments'),
]
