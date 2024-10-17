from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control'}),
            'choice_text': forms.TextInput(attrs={'class': 'form-control'}),
            'votes': forms.NumberInput(attrs={'class': 'form-control'}),
        }