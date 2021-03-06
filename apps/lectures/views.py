from rest_framework import serializers, viewsets
from .models import Lecture

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description', 'lecturer_name', 'date', 'duration', 'level')

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer