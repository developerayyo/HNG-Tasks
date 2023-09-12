from rest_framework import generics
from django.db.models import Q
from personres.models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    # lookup_field = 'identifier'

    # def get_object(self):
    #     identifier = self.kwargs['identifier']
    #     # Check if the identifier is numeric (assume it's an ID)
    #     try:
    #         if identifier.isdigit():
    #             return self.queryset.get(pk=identifier)
    #         # If it's not numeric, assume it's a name
    #         return self.queryset.get(Q(name__icontains=identifier))
    #     except ObjectDoesNotExist:
    #         return None


    # def get_queryset(self):
    #     # Get the base queryset
    #     queryset = super().get_queryset()
        
    #     # Retrieve query parameters from the request URL
    #     name = self.request.query_params.get('name')
        
    #     # Apply filtering based on query parameters&Filter by name (case-insensitive, contains the name)
    #     if name:
    #         queryset = queryset.filter(name__icontains=name)
    #     return queryset

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

