from rest_framework import serializers

from events.models import event_info

class CompanySerializers(serializers.ModelSerializer):
        class Meta:
            model= event_info
            fields =('')
