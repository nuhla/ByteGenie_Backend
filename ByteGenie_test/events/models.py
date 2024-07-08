from django.db import models

class event_info(models.Model):
    event_logo_url = models.TextField()
    event_name = models.CharField(max_length=305)
    event_start_date  = models.CharField(max_length=55)
    event_end_date = models.CharField(max_length=35)
    event_venue = models.CharField(max_length=35)
    event_country = models.CharField(max_length=100)
    event_description = models.TextField()
    event_url = models.TextField()

   