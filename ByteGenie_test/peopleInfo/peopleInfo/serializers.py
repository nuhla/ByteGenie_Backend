from rest_framework import serializers

from peopleInfo.models import people_info 

class CompanySerializers(serializers.ModelSerializer):
        class Meta:
            model= people_info
            fields =('')
