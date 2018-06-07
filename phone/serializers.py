from rest_framework import serializers
from .models import CallStartRecord
from .models import CallEndRecord
from .models import CallReport


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


class CallReportSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = CallReport
        fields = (
            'destination',
            'start_date',
            'start_time',
            'duration',
            'price'
        )
