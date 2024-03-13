from celery import shared_task
from .models import File
from django.core.files.base import ContentFile
from django.conf import settings
import os
import mimetypes


@shared_task
def process_file(file_id):
    file_instance = File.objects.get(id=file_id)
    file_type = mimetypes.guess_type(file_instance.file.path)[0]
    # file_path = file_instance.file.path

    if file_type.startswith('image/'):
        process_image(file_instance.file.path)
    elif file_type.startswith('text/'):
        process_text(file_instance.file.path)
    # with open(file_path, 'a') as file:
    #     file.write("\nfile processed")

    file_instance.processed = True
    file_instance.save()


@shared_task
def process_image(file_path):
    ...


def process_text(file_path):
    with open(file_path, 'a') as file:
        file.write("\nfile processed")