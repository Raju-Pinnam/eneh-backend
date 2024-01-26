from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework import status, permissions, response

from leads.models import Lead, CarearEmployee

class LeadRegisterAPIView(APIView):
    
    def post(self, request):
        data = request.data
        print(data)
        # lead_obj = Lead.objects.create(**data)
        return render(request, 'index.html')
        

class EmployeeApplyView(APIView):
    
    def post(self, request):
        data = request.data
        print(data)
        return render(request, 'careers.html')
