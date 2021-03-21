from rest_framework import serializers
from booking.models import BookingTransaction, Message, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class BookingTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTransaction
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
