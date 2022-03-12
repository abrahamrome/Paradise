from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
	help ='Borra el usuario indicado'
	def add_arguments(self, parser):
		parser.add_argument('username', nargs='+', type=str)

	def handle(self, *args, **options):
		for nombre in options['username']:
			try:
				user= User.objects.get(username=nombre)
			except User.DoesNotExist:
				raise CommandError('Usuario "%c" no existe' %username)

			user.delete()
			self.stdout.write(self.style.SUCCESS('Usuario eliminado con exito'))

			

				