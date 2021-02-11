from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from subjects.course.views import CourseViewSet
from subjects.subject.views import SubjectViewSet

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename = 'course')
router.register(r'subject', SubjectViewSet, basename = 'subject')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
