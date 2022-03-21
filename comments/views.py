from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin

from .models import We
from .serializers import PostSerializers


class PostListAPIView(CreateModelMixin, ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PostSerializers

    def get_queryset(self):
        r = self.request
        print(r.user)
        qs = We.objects.all().order_by('option', 'post')
        print(qs)
        return qs

