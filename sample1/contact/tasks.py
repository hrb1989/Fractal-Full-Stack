from celery import shared_task
from django.core.mail import send_mail

@shared_task
def sendRegMailTask(emailID):
    send_mail(
    'You have been registered',
    'Registration is successfull on the Fractal Portal',
    'noreply@samFractal.com',
    [emailID],
    fail_silently=False,
    )