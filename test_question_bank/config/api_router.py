from django.conf import settings
#from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_mongoengine.routers import DefaultRouter, SimpleRouter

from test_question_bank.users.api.views import UserViewSet
from test_question_bank.math_exercises.api.views import KnowledgePointViewSet, MathExercisesViewSet, \
    FillInBlankExercisesViewSet, TOFExercisesViewSet, ChoiceExercisesViewSet, CalculationExercisesViewSet, \
    WordProblemExercisesViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

#router.register("users", UserViewSet)
router.register('knowledgeP', KnowledgePointViewSet)
router.register('math', MathExercisesViewSet)
router.register('fillinE', TOFExercisesViewSet)
router.register('tofE', TOFExercisesViewSet)
router.register('choiceE', ChoiceExercisesViewSet)
router.register('calcE', TOFExercisesViewSet)
router.register('wordPE', TOFExercisesViewSet)


app_name = "api"
urlpatterns = router.urls
