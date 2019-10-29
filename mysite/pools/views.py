

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice
from django.template import loader
from django.views import generic

# Create your views here.


def index(request):
    question_list = Question.objects.all()
    paginator= Paginator(question_list, 20)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    #order_by("-pub_data")[:5]
    template = loader.get_template("pools/index.html")
    context = {
        'questions': questions
    }
    return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = "pools/index.html"
    context_object_name = "questions"
    model = Question

    def get_queryset(self):
        return Question.objects.order_by('-pub_data')[:5]


def detail(request, question_id):
    # try:
    #    questions = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404("Question nie istnieje")
    questions = get_object_or_404(Question, pk=question_id, pub_data__lt=timezone.now())
    #if questions.pub_data > timezone.now():
            #raise Http404("Zasób nie istnieje")
    # output += str(questions)
    # return HttpResponse(output)
    return render(
        request,
        "pools/details.html",
        {
            'question': questions
        }
    )


def results(request, question_id):
    questions = get_object_or_404(Question, pk=question_id)
    context = {'question': questions}

    # output += str(questions)
    # return HttpResponse(output)
    return render(
        request,
        "pools/results.html",
        context
    )
#return HttpResponse("Wyniki dla pytania %s" % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice_id = request.POST['choice']
    selected_choice = question.choice_set.get(pk=selected_choice_id)
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('pools:results', args=(question_id,)))
