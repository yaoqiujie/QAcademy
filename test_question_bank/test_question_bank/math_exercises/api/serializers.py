# -*- coding: utf-8 -*-
# Author：Qiujie Yao
# Email: yaoqiujie@gscopetech.com
# @Time: 2020/5/22 3:46 下午

from rest_framework_mongoengine import serializers
from test_question_bank.math_exercises.models import KnowledgePoint, MathExercises, FillInBlankExercises, \
    TOFExercises, ChoiceExercises, CalculationExercises, WordProblemExercises


class KnowledgePointSerializer(serializers.DocumentSerializer):
    class Meta:
        model = KnowledgePoint
        fields = '__all__'


class MathExercisesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = MathExercises
        fields = '__all__'


class TOFExercisesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = TOFExercises
        fields = '__all__'


class FillInBlankExercisesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = FillInBlankExercises
        fields = '__all__'


class ChoiceExercisesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ChoiceExercises
        fields = '__all__'


class CalculationExercisesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CalculationExercises
        fields = '__all__'


class WordProblemExercisesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = WordProblemExercises
        fields = '__all__'
