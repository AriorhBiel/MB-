from .models import *
from .serializer import *
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class DateViewSet(viewsets.ModelViewSet):    
    queryset = Date.objects.all()
    serializer_class = DateSerializer