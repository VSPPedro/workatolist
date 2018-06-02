from rest_framework import serializers
from .models import CallStartRecord


class CallStartRecordSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = CallStartRecord
        fields = (
            'id',
            'type',
            'timestamp',
            'call_id',
            'source',
            'destination'
        )
