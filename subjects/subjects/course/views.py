from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer
