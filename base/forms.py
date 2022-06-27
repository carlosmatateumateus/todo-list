from django.forms import ModelForm
from .models import WriteDown

class NoteForm(ModelForm):

    class Meta:
        model = WriteDown
        fields = '__all__'