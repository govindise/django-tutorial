from . import views
from rest_framework import routers
from django.urls import path, include
from .views import QuestionViewSet, ChoiceViewSet, kafkaConsumer

# define the router
router = routers.DefaultRouter()
# define the router path and viewset to be used
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test/', views.test, name='test'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('kafkaproducer/', views.kafkaProducter, name='kafkaproducer'),
    path('kafkaconsumer/', views.kafkaConsumer, name='kafkaconsumer'),
    path('kafkafunction/', views.kafkaFunction, name='kafkafunction'),
]