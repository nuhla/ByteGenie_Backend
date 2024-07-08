from django.db import models


class company_info(models.Model):
    company_logo_url = models.TextField()
    company_logo_text = models.TextField()
    company_name = models.CharField(max_length=200)
    relation_to_event = models.CharField(max_length=100)
    event_url = models.TextField()
    company_revenue = models.CharField(max_length=70)
    n_employees = models.CharField(max_length=200)
    company_phone = models.CharField(max_length=30)
    company_founding_year = models.CharField(max_length=6)
    company_address = models.CharField(300)
    company_industry = models.TextField()
    company_overview = models.TextField()
    homepage_url = models.TextField()
    linkedin_company_url= models.TextField()
    homepage_base_url = models.TextField()
    company_logo_url_on_event_page = models.TextField()
    company_logo_match_flag = models.TextField()

