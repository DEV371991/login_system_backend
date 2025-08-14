from django.urls import path
from .views import RegisterView, CourseListView, EnrollView
# from .views import MyTokenObtainPairView
from .views import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('enroll/', EnrollView.as_view(), name='enroll'),
    # path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', LoginView.as_view(), name='login'),

]
