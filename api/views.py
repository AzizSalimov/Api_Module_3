from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from api import serializers
from api.models import Post, Comment, Category
from api.permissions import IsOwnerOrReadOnly
from api.serializers import PostSerializer

from rest_framework import generics, viewsets
from .serializers import CategorySerializer
from paginations import CustomPageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer

from rest_framework import viewsets
from rest_framework.decorators import action


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['patch'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes += 1
        post.save()
        serializers = self.get_serializer(post)
        return Response(serializers.data)

    @action(detail=True, methods=['patch'])
    def dislike(self, request, pk=None):
        post = self.get_object()
        post.dislikes += 1
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("category", "brand")
    ordering_fields = ("id", "price")
    search_fields = ("title", "category__title", "brand__title")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CategorySerializer
        return CategorySerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name']
#
#     def get_queryset(self):
#         # Customize the queryset if needed
#         return super().get_queryset()
#
#     def perform_create(self, serializer):
#         # Perform additional actions during object creation if needed
#         serializer.save()
#
#     def perform_update(self, seri
#     alizer):
#         # Perform additional actions during object update if needed
#         serializer.save()
#
#     def perform_destroy(self, instance):
#         # Perform additional actions during object deletion if needed
#         instance.delete()


class PostLists(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']
    ordering = ['-created_at']
    pagination_class = LimitOffsetPagination
