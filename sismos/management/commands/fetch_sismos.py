from django.core.management.base import BaseCommand
from sismos.tasks import load_features_from_usgs


class Command(BaseCommand):
    help = "Obtiene y guarda los datos de sismos desde USGS"

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando carga de datos sísmicos...")
        load_features_from_usgs()
        self.stdout.write(self.style.SUCCESS("Carga completada con éxito."))
