from .models import CallStartRecord, CallEndRecord, CallReport
from .serializers import CallStartRecordSerializer
from .serializers import CallEndRecordSerializer
from .serializers import CallReportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
import datetime


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


@api_view(http_method_names=['GET'])
def last_bill(request, phone_number):

    year = datetime.datetime.now().year
    previous_month = datetime.datetime.now().month - 1
    period = "{0}/{1:02d}".format(year, previous_month)
    queryset = CallReport.objects.filter(source=phone_number,
                                         start_date__year=year,
                                         start_date__month=previous_month)
    response_json = {}

    if len(queryset) == 0:
        response_json = {
            "The phone '{0}' does not have call records for the period of {1}."\
            .format(phone_number, period)
        }
    else:
        response_json = build_json(phone_number, period, queryset)

    return Response(response_json)


@api_view(http_method_names=['GET'])
def bill(request, phone_number, year, month):

    period = "{0}/{1:02d}".format(year, month)
    queryset = CallReport.objects.filter(source=phone_number,
                                         start_date__year=year,
                                         start_date__month=month)
    response_json = {}

    if len(queryset) == 0:
        response_json = {
            "The phone '{0}' does not have call records for the period of {1}."\
            .format(phone_number, period)
        }
    else:
        print(queryset[0].price)
        response_json = build_json(phone_number, period, queryset)

    return Response(response_json)


def build_json(phone_number, period, queryset):

    serializer = CallReportSerializer(queryset, many=True)

    response_json = {
        "subscriber": phone_number,
        "period": period,
        "calls": serializer.data
    }

    return response_json
