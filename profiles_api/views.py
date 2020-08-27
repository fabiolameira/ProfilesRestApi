from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as functions (Get, Post, Put, Patch and Delete)',
            'Is similar to a tradicional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})