from .models import CallStartRecord, CallEndRecord
from .serializers import CallStartRecordSerializer
from .serializers import CallEndRecordSerializer
from rest_framework import viewsets


class CallStartRecordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = CallStartRecord.objects.all()
    serializer_class = CallStartRecordSerializer


class CallEndRecordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = CallEndRecord.objects.all()
    serializer_class = CallEndRecordSerializer
