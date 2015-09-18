from django.db import models

# ============================================================================

class TimeTrackModel(models.Model):
    """Abstract model with auto-updating create & update timestamp fields.

    :param created:
        Date/time when the model was created
    :param updated:
        Date/time when the model was last updated
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
