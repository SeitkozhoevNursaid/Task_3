from celery import shared_task
from django.core.mail import send_mail
from music.models import Music


@shared_task
def music_created(id, name):
    
    subject = f'Ваш номер песни {id}'
    message = f'Вы успешно создали песню, название вашей песни:{name}'
    mail_sent = send_mail(subject,
                          message,
                          'nursaid.seitkozhoev@mail.ru',
                          ['nursaid.seitkozhoev@mail.ru'])
    return mail_sent

#Функцию вызывать в сериализаторе и упростить код
#Мне нужно с сериализатора в селери функцию передавать названия чтобы заново не вытаскивать обьект
