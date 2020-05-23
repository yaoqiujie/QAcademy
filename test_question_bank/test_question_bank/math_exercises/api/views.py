# -*- coding: utf-8 -*-
# Author：Qiujie Yao
# Email: yaoqiujie@gscopetech.com
# @Time: 2020/5/22 3:46 下午

from rest_framework_mongoengine import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from test_question_bank.math_exercises.models import KnowledgePoint, MathExercises, FillInBlankExercises, \
    TOFExercises, ChoiceExercises, CalculationExercises, WordProblemExercises
from .serializers import KnowledgePointSerializer, MathExercisesSerializer, FillInBlankExercisesSerializer, \
    TOFExercisesSerializer, ChoiceExercisesSerializer, CalculationExercisesSerializer, WordProblemExercisesSerializer


class CustomerPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class KnowledgePointViewSet(viewsets.ModelViewSet):
    queryset = KnowledgePoint.objects.all()
    serializer_class = KnowledgePointSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


class MathExercisesViewSet(viewsets.ModelViewSet):
    queryset = MathExercises.objects.all()
    serializer_class = MathExercisesSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


class FillInBlankExercisesViewSet(viewsets.ModelViewSet):
    queryset = FillInBlankExercises.objects.all()
    serializer_class = FillInBlankExercisesSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


class TOFExercisesViewSet(viewsets.ModelViewSet):
    queryset = TOFExercises.objects.all()
    serializer_class = TOFExercisesSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


class ChoiceExercisesViewSet(viewsets.ModelViewSet):
    queryset = ChoiceExercises.objects.all()
    serializer_class = ChoiceExercisesSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


class CalculationExercisesViewSet(viewsets.ModelViewSet):
    queryset = CalculationExercises.objects.all()
    serializer_class = CalculationExercisesSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


class WordProblemExercisesViewSet(viewsets.ModelViewSet):
    queryset = WordProblemExercises.objects.all()
    serializer_class = WordProblemExercisesSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomerPagination


