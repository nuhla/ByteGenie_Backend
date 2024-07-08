from django.db import models

class people_info(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    person_city = models.CharField(max_length=50)
    person_state =models.CharField(max_length=50)
    person_country = models.CharField(max_length=50)
    email_pattern = models.CharField(max_length=100)
    homepage_base_url = models.CharField(max_length=150)
    duration_in_current_job = models.CharField(300)
    duration_in_current_company =models.CharField(300)
   