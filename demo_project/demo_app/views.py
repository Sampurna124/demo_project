from rest_framework.views import APIView
from rest_framework.response import Response

class FirstApi(APIView):
    def get(self,request):
        return Response(data={'detail':'Get method '})
