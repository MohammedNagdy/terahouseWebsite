from django.shortcuts import render
from django.views import View
from .models import Order
from terahouse_project.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail



# order --> prices section in html
class OrderListView(View):
    template = "terahouse_project/index.html"
    success_template = 'terahouse_project/success.html'
    queryset = Order.objects.all()

    # the products
    def get(self, request):
        context = {'obj_list': self.queryset}
        return render(request, self.template, context)


class ContactUsView(View):
    template = "terahouse_project/contact_form.html"
    success_template ='terahouse_project/success.html'
    def get(self, request):
        contact = forms.ContactUsForm()
        context = { 'form': contact}
        return render(request, self.template, context)

    def post(self, request):
        contact = forms.ContactUsForm()
        context = { 'form': contact}

        # sending email that tells we'll respond as soon as possible
        contact = forms.ContactUsForm(request.POST or None)
        if request.method == 'POST':
            if contact.is_valid():
                recepient = str(contact['email'].value())
                name_user = str(contact['name'].value())
                message_user = str(contact['message'].value())
                subject = f'Welcome {name_user} to Terahouse'
                message = f'We will respond to you as soon as possible. Regarding "{message_user}"'
                send_mail(subject,
                    message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                return render(request, self.success_template, {'recepient': recepient})
            contact = forms.ContactUsForm()
        return render(request, self.template, context)
