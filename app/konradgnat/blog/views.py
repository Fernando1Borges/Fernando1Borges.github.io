from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.template import loader

from django.views import generic 

from .models import Post
from .models import Room
from .models import Message
from .models import Book
from .models import Project
from .serializers import *

def home(request):
    template_name = 'index.html'
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class BooksList(generic.ListView):
    queryset = Book.objects.filter(status=1).order_by('-read_on')
    template_name = 'books.html'

class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class ProjectsList(generic.ListView):
    queryset = Project.objects.filter(status=1).order_by('-built_on')
    template_name = 'projects.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

# TODO: create project templates

# TODO: create a React front end for a chat room
# TODO: consider if this is a good idea, might prefer to scrap this chat room project

# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == 'GET':
#         data = Post.objects.all()

#         serializer = PostSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def room_list(request):
#     if request.method == 'GET':
#         data = Room.objects.all()

#         serializer = RoomSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RoomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

