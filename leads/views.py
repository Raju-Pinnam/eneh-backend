from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status, permissions, response

from leads.models import Lead

class LeadRegisterAPIView(APIView):
    
    def post(self, request):
        data = request.data
        print(data)
        # lead_obj = Lead.objects.create(**data)
        return response.Response(
            "Working",
            status=status.HTTP_201_CREATED
        )
        
