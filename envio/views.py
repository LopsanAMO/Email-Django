from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Formulario, FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
class Enviar(View):
    def get(self, request):
        template_name = 'contacto_mail.html'
        form = Formulario()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        form = Formulario(request.POST)
        if form.is_valid():
            return redirect('correo:home')
        else:
            return redirect('correo:enviar')

def Home(request):
    return render(request, 'index.html', {})

class ContactoMail(View):
    def get(self, request):
        template_name = 'contacto_mail.html'
        form = FormularioContacto()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        form = FormularioContacto(request.POST)
        if form.is_valid():
            asunto = 'Este es un mensaje de mi BLOG con DJANGO'
            mensaje = form.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=['info@zastask.com'])
            mail.send()
        return redirect('correo:home')
