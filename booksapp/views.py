from django.shortcuts import render
from rest_framework import viewsets
from .models import Loan , Customer , Book
from .serializers import CustomerSerializer,BookSerializer ,LoanSerializer
# Create your views here.

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LoanView(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
