from rest_framework import serializers
from .models import Book , Customer , Loan


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'             

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['books'] = BookSerializer(instance.books,many=True).data
        data['customer'] = CustomerSerializer(instance.customer).data
        return data