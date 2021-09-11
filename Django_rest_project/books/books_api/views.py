from rest_framework.views import APIView
from rest_framework.response import Response

class BookListCreate(APIView):
    def get(self, request):
        return Response({'message': 'ok'})

    def post(self, request):
        pass