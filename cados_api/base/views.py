from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q


from .models import Advocate
from .serializer import AdvocateSerializer

# Create your views here.
@api_view()
def endopoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocates_list(request):
    if request.method == 'GET':
        # data = ['Dannis', 'Tadas', 'Maz']
        advocates = Advocate.objects.all()
        query = request.query_params.get('query')
        if query:
            advocates = advocates.filter(Q(username__contains = query) | Q(bio__contains = query ) )
        serialized_item = AdvocateSerializer(advocates, many=True)
        return Response(serialized_item.data)
    
    if request.method == 'POST':
        advocates = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
            )
        serialized_item = AdvocateSerializer(advocates)
        return Response(serialized_item.data)

@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
    advocate = get_object_or_404(Advocate, username=username)

    if request.method == 'GET':
        serialized_item = AdvocateSerializer(advocate)
        return Response(serialized_item.data)
    
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()

        serialized_item = AdvocateSerializer(advocate)
        return Response(serialized_item.data)   

    if request.method == 'DELETE':
        advocate.delete()
        return Response({"message" : "user was deleted"})