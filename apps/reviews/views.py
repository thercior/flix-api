from rest_framework import response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer

# Create your views here.
class ReviewCreateListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        success_message = "Este Review foi excluído com sucesso!"
        return response.Response({"message": success_message})
        