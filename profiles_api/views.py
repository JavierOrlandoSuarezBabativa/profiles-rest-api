from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions',
            'Is similar to Django View',
            'Gives you the most over the app logic',
            'Is mapped manually to URLs'
        ]

        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })