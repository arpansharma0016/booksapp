from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def index(request):
    return render(request, "index.html")

@csrf_exempt
def send(request, email, username):
    try:
        html_content = render_to_string("email.html", {'username': username})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            f"Booksapp Internship Task",
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )

        email.attach_alternative(html_content, "text/html")
        email.send()
        return JsonResponse({"status":'success'})

    except:
        return JsonResponse({"status":'error'})
