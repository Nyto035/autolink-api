import os

from django.conf import settings
from rest_framework.decorators import api_view
from sendfile import sendfile


@api_view()
def serve_media(request, path):
    actual_path = os.path.join(settings.MEDIA_ROOT, path)
    return sendfile(request, actual_path, attachment=True)
