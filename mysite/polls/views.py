# Create your views here.
# importing task from tasks.py file
from .task import test_func
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Question, Choice
from rest_framework import permissions
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import QuestionSerializer, ChoiceSerializer


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def test(request):
    # call the test_function using delay, calling task  
    print(test_func.delay())
    return HttpResponse("Done")


# create a viewset
class QuestionViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Question.objects.all().order_by('question_text')
    # specify serializer to be used
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


# create a viewset
class ChoiceViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Choice.objects.all()
    # specify serializer to be used
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
from json import dumps
from time import sleep


def kafkaProducter(request) :
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'),
                            api_version=(0, 10, 1))
    
    serialized_data = {'KafkaProducer' : 'Hi'}
    producer.send('temp', value=serialized_data)        

    return HttpResponse(serialized_data)


def kafkaConsumer(request) :
    consumer = KafkaConsumer('temp',
                            bootstrap_servers=['localhost:9092'],
                            value_deserializer=lambda x: loads(x.decode('utf-8')),
                            api_version=(0, 10, 1))
    deserialized_data = []
    for message in consumer :
        deserialized_data.append(message.value)
    
    print(deserialized_data)
    return HttpResponse({'KafkaConsumer':str(deserialized_data)})


def kafkaFunction(request):
  from kafka import KafkaProducer
  producer = KafkaProducer(bootstrap_servers='localhost:9092',
                           value_serializer=lambda x: dumps(x).encode('utf-8'))
  producer.send('foobar', b'test')
  return HttpResponse(200)