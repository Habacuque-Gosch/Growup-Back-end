from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.rest_api.models import Item
from apps.rest_api.serializers import ItemSerializer
# from django.contrib.auth import login
# import json




@api_view(['GET'])
def get_all_users(request):

    if request.method == 'GET':

        try:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)

            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404)

@api_view(['GET'])
def get_by_name(request, name):

    try:
        user = Item.objects.get(name=name)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = ItemSerializer(user)
        return Response(serializer.data)
    
@api_view(['GET','POST', 'PUT', 'DELETE'])
def user_manager(request):

    # GET DATA USER
    if request.method == 'GET':

        try:
            if request.GET['name']:

                name = request.GET['name']

                try:
                    user = Item.objects.get(name=name)
                except:
                    print('user not found')
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = ItemSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # MAKE DATA USER
    if request.method == 'POST':

        new_user = request.data

        serializer = ItemSerializer(data=new_user)
        if serializer.is_valid():
            print('Make User')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)  

    # EDITING USER
    if request.method == 'PUT':

        user = request.data['name']
        update_user = Item.objects.get(name=user)

        serializer = ItemSerializer(update_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # DELETING USER
    if request.method == 'DELETE':
        
        try:
            user_to_delete = Item.objects.get(name=request.data['name'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)