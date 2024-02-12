from django.core.management.base import BaseCommand
from datetime import datetime
from atores.models import Ator
import csv


# Command para importar dados de arquivos externos
class Command(BaseCommand):
    # Adiciona argumantos ao meu command
    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            type=str,
            help='Nome do arquivo CSV/XLSX com atores',
        )

    def handle(self, *args, **options):
        filename = options['filename']

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                nome = row['nome']
                nascimento = datetime.strptime(row['nascimento'], '%Y-%m-%d').date()
                nacionalidade = row['nacionalidade']

                self.stdout.write(self.style.NOTICE(nome)) # informa qual dado está sendo adicionado no momento

                Ator.objects.create(
                    nome=nome,
                    nascimento=nascimento,
                    nacionalidade = nacionalidade,
                )

        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))