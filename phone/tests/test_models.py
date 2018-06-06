from django.test import TestCase
from phone.models import CallStartRecord
from phone.models import CallEndRecord
from phone.models import CallReport


class CallStartRecordTest(TestCase):
    """This class defines the suite for the CallStartRecord model."""

    def setUp(self):
        """Define the variables."""
        self.call_start_record = CallStartRecord(
            call_id=70,
            source="99988526423",
            destination="9993468278",
            timestamp="2016-02-29T12:00:00Z",
            type="start"
        )

    def test_model_can_create_a_call_start_record(self):
        """Test the CallStartRecord model can create a call start record."""
        old_count = CallStartRecord.objects.count()
        self.call_start_record.save()
        new_count = CallStartRecord.objects.count()
        self.assertNotEqual(old_count, new_count)


class CallEndRecordTest(TestCase):
    """This class defines the suite for CallEndRecord model."""

    def setUp(self):
        """Define the variables."""
        self.call_end_record = CallEndRecord(
            call_id=70,
            timestamp="2016-02-29T14:00:00Z",
            type="end"
        )

    def test_model_can_create_a_call_end_record(self):
        """Test the CallEndRecord model can create a call end record."""
        old_count = CallEndRecord.objects.count()
        self.call_end_record.save()
        new_count = CallEndRecord.objects.count()
        self.assertNotEqual(old_count, new_count)


class CallReportTest(TestCase):
    """This class defines the suite for CallReport model."""

    def setUp(self):
        """Define the variables."""
        self.call_start_record = CallStartRecord(
            call_id=70,
            source="99988526423",
            destination="9993468278",
            timestamp="2016-02-29T12:00:00Z",
            type="start"
        )
        self.call_end_record = CallEndRecord(
            call_id=70,
            timestamp="2016-02-29T14:00:00Z",
            type="end"
        )

    def test_model_can_create_a_call_report(self):
        """Test the CallReport model can create a call report."""
        old_count = CallReport.objects.count()
        self.call_start_record.save()
        self.call_end_record.save()
        new_count = CallReport.objects.count()
        self.assertNotEqual(old_count, new_count)
