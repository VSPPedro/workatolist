from django.db import models
from datetime import datetime


class CallRecord(models.Model):
    """This class represents the CallRecord model."""
    call_id = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        This makes the CallRecord to become abstract and sets the default
        sorting order to 'created_at' when listing this objects.
        """
        abstract = True
        ordering = ('created_at',)


class CallStartRecord(CallRecord):
    """This calss represents the CallStartRecord model."""
    source = models.CharField(max_length=11)
    destination = models.CharField(max_length=11)
    type = models.CharField(max_length=5, default="start")


class CallEndRecord(CallRecord):
    """This calss represents the CallEndRecord model."""
    type = models.CharField(max_length=5, default="end")
