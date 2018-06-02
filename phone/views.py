from .models import CallStartRecord
from .serializers import CallStartRecordSerializer
from rest_framework import viewsets


class CallStartRecordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = CallStartRecord.objects.all()
    serializer_class = CallStartRecordSerializer
