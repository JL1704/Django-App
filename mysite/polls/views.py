from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView

from .forms import QuestionForm, ChoiceForm
from .models import Choice, Question

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'  # Cambia 'latest_question_list' a 'question_list'

    # Ajusta el queryset para que recupere todas las encuestas
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))    

def question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save() 
            return render(request, 'polls/success.html', {'question_text': question.question_text})
    else:
        form = QuestionForm()

    return render(request, 'polls/question_form.html', {'form': form})
      
def success_view(request):
    return render(request, 'polls/success.html')

def create_choice_view(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:success_choice')
    else:
        form = ChoiceForm()

    return render(request, 'polls/create_choice.html', {'form': form})


def success_choice_view(request):
    return render(request, 'polls/success_choice.html')