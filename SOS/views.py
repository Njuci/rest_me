from rest_framework.response import Response
from rest_framework import status
from .models import Hopitals
from .serializers import hospitalsSerializers
from rest_framework.views import APIView

class UnseulHopital(APIView):

    def get(self,request,id):
        try:
            hospital = Hopitals.objects.get(id=id)
            serial = hospitalsSerializers(hospital)
        except:
            message={"msg":"id inexitant"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        return Response(serial.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            hospital = Hopitals.objects.get(id=id)
            serial = hospitalsSerializers(hospital)
        except:
            message = {"msg": "id inexitant"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


class touslesHopital(APIView):

    def get(self, request):
        hospitals = Hopitals.objects.all()
        serial = hospitalsSerializers(hospitals, many=True)
        return Response(serial.data)

    def post(self, request):
        serializer = hospitalsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

