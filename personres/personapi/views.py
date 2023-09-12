from rest_framework import generics
from django.db.models import Q
from personres.models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
from django.http import JsonResponse


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

# class PersonListCreateView(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonSearchByNameView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PersonSerializer
#     lookup_field = 'name'
    
#     def get_queryset(self):
#         name = self.kwargs['name']  # Assuming you pass the name in the URL parameter
#         queryset = Person.objects.filter(Q(name__icontains=name))
#         return queryset
    
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()

    #     if not queryset.exists():
    #         # Return a 404 response with a custom error message
    #         return JsonResponse({'error': 'No matching persons found for the given name.'})
        
    #     serializer = self.get_serializer(queryset, many=True)
    #     return JsonResponse(serializer.data, safe=False)

