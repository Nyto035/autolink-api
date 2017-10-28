from django.core.management import BaseCommand

from bina_bikers.pg_search.utils import populate_models_document_field


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        populate_models_document_field()
