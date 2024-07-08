from rest_framework import serializers

from company.models import company_info 

class CompanySerializers(serializers.ModelSerializer):
        class Meta:
            model= company_info
            fields =('')
