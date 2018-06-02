from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from phone.models import CallStartRecord
from phone.serializers import CallStartRecordSerializer
import json


class CallStartRecordViewSetTest(TestCase):
    """Test suit for the CallStartRecordViewSet."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.call_start_record_data = {
            'call_id': '70',
            'source': '99988526423',
            'destination': '9993468278',
            'timestamp': '2016-02-29T12:00:00Z',
            'type': 'start'
        }
        self.response = self.client.post(
            '/call-start-records/',
            self.call_start_record_data,
            format="json"
        )

    def test_api_can_create_a_call_start_record(self):
        """Test the api has call start record creation capability."""
        self.assertEqual(
            self.response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(CallStartRecord.objects.count(), 1)

    def test_api_can_get_a_call_start_record(self):
        """Test the api can get a given call start record."""
        call_start_record = CallStartRecord.objects.get()
        serializer = CallStartRecordSerializer(call_start_record)
        response = self.client.get(
            '/call-start-records/%d/' % call_start_record.id,
            format="json"
        )
        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content, serializer.data)

    def test_api_can_update_call_start_record(self):
        """Test the api can update a given call start record."""
        call_start_record = CallStartRecord.objects.get()
        new_destination = '9999999999'
        call_start_record.destination = new_destination
        serializer = CallStartRecordSerializer(call_start_record)
        serializer_data = serializer.data
        response = self.client.put(
            '/call-start-records/%d/' % call_start_record.id,
            serializer_data,
            format="json"
        )

        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            content['destination'], new_destination
        )

    def test_api_can_delete_call_start_record(self):
        """Test the api can delete a call start record."""
        old_count = CallStartRecord.objects.count()
        call_start_record = CallStartRecord.objects.get()
        response = self.client.delete(
            '/call-start-records/%d/' % call_start_record.id,
            format="json",
            follow=True
        )
        new_count = CallStartRecord.objects.count()

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertNotEqual(old_count, new_count)
