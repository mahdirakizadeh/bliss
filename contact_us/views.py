from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


class ContactView(View):
    form_class = ContactForm

    def get(self, request):
        contact = self.form_class()
        return render(request, 'contact_us/contact.html', {'contact': contact})

    def post(self, request):
        contact = ContactForm(request.POST)
        if contact.is_valid():
            cd = contact.cleaned_data
            subject = "Contact With User!"
            body = {
                'fullname': cd['full_name'],
                'email': cd['email'],
                'phone_number': cd['phone_number'],
                'message': cd['message']
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'mahdirr80@gmail.com', ['mahdirr80@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home:home')

        return render(request, 'home/index.html', {'contact': contact})
