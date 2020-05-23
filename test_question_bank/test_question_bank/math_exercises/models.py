from django.utils.translation import ugettext_lazy as _
import mongoengine as me
import datetime

# Create your models here.


class KnowledgePoint(me.Document):
    title = me.StringField(max_length=128, required=True, unique=True)
    detail = me.StringField(max_length=2048,)
    video = me.ListField(me.URLField())


class MathExercises(me.Document):
    GRADE_CHOICES = (
        ('ONE', _('Grade One')),
        ('TWO', _('Grade Two')),
        ('THREE', _('Grade Three')),
        ('FOUR', _('Grade Four')),
        ('FIVE', _('Grade Five')),
    )
    STATUS_CHOICES = (
        ('A', _('APPROVED')),
        ('P', _('PENDING')),
        ('R', _('REJECTED')),
        ('D', _('DEPRECATED')),
    )
    TYPE_CHOICES = (
        ('F', _('Fill in blank')),
        ('T', _('True or false')),
        ('C', _('Choice')),
        ('CA', _('Calculation ')),
        ('W', _('Word problems'))
    )
    grade = me.StringField(max_length=8, choices=GRADE_CHOICES, required=True)
    knowledge_point = me.ReferenceField(KnowledgePoint)
    status = me.StringField(max_length=2, choices=STATUS_CHOICES, default='P')
    #type = me.StringField(max_length=2, choices=TYPE_CHOICES, default='W')
    question = me.StringField(max_length=1024, required=True)
    question_image = me.ImageField(size=(800, 600, True), thumbnail_size=(200, 150, False))
    question_in_perseus = me.StringField(max_length=2048, default='')
    answer_image = me.ImageField(size=(800, 600, True), thumbnail_size=(200, 150, False))
    answer_in_perseus = me.StringField(max_length=2048, default='')
    updated = me.DateTimeField(default=datetime.datetime.utcnow)
    created = me.DateTimeField(default=datetime.datetime.utcnow)
    creator = me.StringField(max_length=128, default='Qiujie Yao')

    meta = {
        'collection': 'math_exercises',
        'allow_inheritance': True,
        'ordering': ['-updated', '-created'],
    }


class FillInBlankExercises(MathExercises):
    answer = me.ListField(me.StringField(max_length=64))


class TOFExercises(MathExercises):
    answer = me.BooleanField()


class ChoiceExercises(MathExercises):
    question_choices = me.DictField()
    answer = me.StringField(max_length=8)


class CalculationExercises(MathExercises):
    answer = me.StringField(max_length=64)


class WordProblemExercises(MathExercises):
    answer = me.ListField(me.StringField(max_length=1024))
