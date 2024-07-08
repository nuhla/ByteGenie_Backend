from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 

from django.http.response import JsonResponse
from company.models import company_info 
from company.serializers import CompanySerializers

@csrf_exempt
def CompanyApi(request, id):
    if request.method =='GET':
        companyInfo = company_info.objects.all()
        companySerializers = companySerializers(companyInfo, many=True)
        return JsonResponse(companySerializers.data, safe=False)
