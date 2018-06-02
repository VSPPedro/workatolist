from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from phone.models import CallStartRecord, CallEndRecord
from phone.serializers import CallStartRecordSerializer
from phone.serializers import CallEndRecordSerializer
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


class CallEndRecordViewSetTest(TestCase):
    """Test suit for the CallEndRecordViewSet."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.call_end_record_data = {
            'call_id': '70',
            'timestamp': '2016-02-29T14:00:00Z',
            'type': 'end'
        }
        self.response = self.client.post(
            '/call-end-records/',
            self.call_end_record_data,
            format="json"
        )

    def test_api_can_create_a_call_end_record(self):
        """Test the api has call end record creation capability."""
        self.assertEqual(
            self.response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(CallEndRecord.objects.count(), 1)

    def test_api_can_get_a_call_end_record(self):
        """Test the api can get a given call end record."""
        call_end_record = CallEndRecord.objects.get()
        serializer = CallEndRecordSerializer(call_end_record)
        response = self.client.get(
            '/call-end-records/%d/' % call_end_record.id,
            format="json"
        )
        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content, serializer.data)

    def test_api_can_update_call_end_record(self):
        """Test the api can update a given call end record."""
        call_end_record = CallEndRecord.objects.get()
        new_timestamp = "2016-02-29T14:00:01Z"
        call_end_record.timestamp = new_timestamp
        serializer = CallEndRecordSerializer(call_end_record)
        serializer_data = serializer.data
        response = self.client.put(
            '/call-end-records/%d/' % call_end_record.id,
            serializer_data,
            format="json"
        )

        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            content['timestamp'], new_timestamp
        )

    def test_api_can_delete_call_end_record(self):
        """Test the api can delete a call end record."""
        old_count = CallEndRecord.objects.count()
        call_end_record = CallEndRecord.objects.get()
        response = self.client.delete(
            '/call-end-records/%d/' % call_end_record.id,
            format="json",
            follow=True
        )
        new_count = CallEndRecord.objects.count()

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertNotEqual(old_count, new_count)
