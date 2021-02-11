from rest_framework import viewsets
from .serializers import SubjectSerializer
from .models import Subject

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('name')
    serializer_class = SubjectSerializer
