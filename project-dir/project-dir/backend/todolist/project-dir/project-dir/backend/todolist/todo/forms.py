from django import forms
from django.forms import ModelForm
from .models import List, Todo


class AddToList(forms.ModelForm):
    class Meta:
        model = List
        fields = [
                   'title',
                   'description',
                   'owner',
        ]

class AddToTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
                   'list',
                   'title',
                   'description',
                   'done',
        ]

class ChangeList(forms.ModelForm):
    class Meta:
      model = List
      fields = [
                  'title',
                  'description',
                  'owner',

        ]

class ChangeTodo(forms.ModelForm):
    class Meta:
      model = Todo
      fields = [
                  'list',
                  'title',
                  'description',
                  'done'
        ]
