from django.shortcuts import render

# Create your views here.
from app.models import *

from app.serializers import *

from rest_framework.views import APIView

from rest_framework.response import Response

class ProductData(APIView):
    def get(self,request,Pid):
        #PQO=Product.objects.all()
        #PJD=ProductModelSerializer(PQO,many=True)
        PQO=Product.objects.get(Pid=Pid)
        PJD=ProductModelSerializer(PQO)
        return Response(PJD.data)
    
    def post(self,request):
        CJSD=request.data
        PD=ProductModelSerializer(data=CJSD)
        if PD.is_valid():
            PD.save()

            return Response({'message':'Product is Created'})
        else:
            return Response({'Failed':'Product is not created'})


    def put(self,request,Pid):
        CJSD=request.data
        PO=Product.objects.get(Pid=CJSD['Pid'])
        PD=ProductModelSerializer(PO,data=CJSD)
        if PD.is_valid():
            PD.save()

            return Response({'message':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})
        

    def patch(self,request,Pid):
        CJSD=request.data
        PO=Product.objects.get(Pid=CJSD['Pid'])
        PD=ProductModelSerializer(PO,data=CJSD,partial=True)
        if PD.is_valid():
            PD.save()

            return Response({'message':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})
        
    def delete(self,request,Pid):
        PO=Product.objects.get(Pid=Pid)
        PO.delete()
        return Response({'message':'Product is Deleted'})
