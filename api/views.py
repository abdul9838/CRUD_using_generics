from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer
class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer