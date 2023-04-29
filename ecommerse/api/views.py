from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Product
from .serializers import ProductSerializer

# Define a viewset for the Product model
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    # Define the queryset to be all products
    queryset = Product.objects.all()
    # Use the ProductSerializer to serialize/deserialize products
    serializer_class = ProductSerializer

    # Handle POST requests to create a new product
    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    # Handle GET requests to retrieve a specific product
    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
     # Handle PUT requests to update a specific product
    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
     # Handle DELETE requests to delete a specific product
    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)
