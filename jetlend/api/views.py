from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Passport, Document
from .permissions import IsOwnerOrReadOnly
from .serializers import *


class PassportView(APIView):
    parser_class = (MultiPartParser, FormParser)

    def get(self, request):
        passport = get_object_or_404(Passport, pk=request.user)
        serializer = PassportSerializer(passport)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        return Response(serializer.data)

    def post(self, request):
        passport = PassportSerializer(data=request.data)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        if passport.is_valid():
            passport.save(investor=request.user)
            return Response(passport.data, status=201)
        else:
            return Response(passport.errors, status=400)


class DocumentView(APIView):
    parser_class = (MultiPartParser, FormParser)

    def get(self, request):
        document = get_object_or_404(Document, investor_id=request.user)
        serializer = DocumentSerializer(document)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        return Response(serializer.data)

    def post(self, request):
        document = DocumentSerializer(data=request.data)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        if document.is_valid():
            document.save(investor=request.user)
            return Response(document.data, status=201)
        else:
            return Response(document.errors, status=400)


class QualificationView(APIView):
    def get(self, request):
        qualification = get_object_or_404(Qualification, investor_id=request.user)
        serializer = QualificationSerializer(qualification)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        return Response(serializer.data)


class QualificationRulesView(APIView):
    def put(self, request):
        qualification = get_object_or_404(Qualification, investor_id=request.user)
        serializer = QualificationSerializer(qualification)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        if request.data['rules'] == 'True':
            qualification.rules = True
            qualification.status = 'Level 2'
            qualification.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class QualificationAcceptView(APIView):
    def put(self, request):
        qualification = get_object_or_404(Qualification, investor_id=request.user)
        serializer = QualificationSerializer(qualification)
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        if request.data['accept'] == 'True':
            qualification.status = 'Confirm'
            qualification.save()
            return Response(serializer.data, status=201)
        elif request.data['accept'] == 'False':
            qualification.status = 'Failure'
            qualification.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
