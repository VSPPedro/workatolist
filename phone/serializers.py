from rest_framework import serializers
from .models import CallStartRecord
from .models import CallEndRecord


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


class CallEndRecordSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = CallEndRecord
        fields = (
            'id',
            'type',
            'timestamp',
            'call_id'
        )
