from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TaskModel
from .serializers import TastModelSerializer

@api_view(['GET','POST'])
def taskListAPI(request):

    if request.method=="GET":
        queryset = TaskModel.objects.all()
        serializers = TastModelSerializer(queryset,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    if request.method=="POST":
        serializers = TastModelSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','PATCH','DELETE'])
def tastDetailAPI(request,task_id):
    queryset = TaskModel.objects.get(id=task_id)
    if request.method=="GET":
        serializer = TastModelSerializer(queryset)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    if request.method=="PUT":
        serializer = TastModelSerializer(queryset,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=="PATCH":
        serializer = TastModelSerializer(queryset,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        queryset.delete()
        return Response({'message':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)