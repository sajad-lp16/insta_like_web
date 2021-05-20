from time import sleep

from celery.task import task
from django.contrib.auth import get_user_model

User = get_user_model()


@task(name='Send phone verification code')
def send_phone_verification_code(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    sleep(10)
    print('The code was sent for {}'.format(username))
    return username


@task(name='Send email verification code')
def send_email_verification_code(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    sleep(10)
    print('The code was sent for {}'.format(email))
    return email
