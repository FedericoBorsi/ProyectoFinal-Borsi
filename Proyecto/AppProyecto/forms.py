from django import forms
from django.contrib.auth.models import User
from datetime import datetime


"""
class PosteoForm(forms.Form):
    titulo = forms.CharField(label = "titulo", max_length = 50)
    subtitulo = forms.CharField(label = "subtitulo", max_length = 50)
    cuerpo = forms.CharField(label = "cuerpo", widget = forms.Textarea)
    autor = forms.CharField(label = "autor", max_length = 50)
    fecha = forms.DateField(label = "fecha", widget = forms.SelectDateWidget)
    imagen = forms.ImageField(label = "imagen")
    """

class MensajeriaForm(forms.Form):
    receptor = forms.ChoiceField(label = "receptor", choices = [(user.username, user.username) for user in User.objects.all()])
    mensaje = forms.CharField(label = "mensaje", widget = forms.Textarea)
    fecha = forms.DateTimeField(label = "fecha", initial = datetime.now())
