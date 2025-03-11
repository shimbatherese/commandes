from django.contrib import admin
from app_commande.models import Clients, Commande
# Register your models here.

admin.site.register(Clients, list_display=('numero','nom','postnom','prenom','sexe','adresse','telephone','e_mail','commande'),search_fields=['numero','nom','postnom','prenom','sexe','adresse','telephone','e_mail','commande'], list_filter=['commande'])
admin.site.register(Commande, list_display=['code','libelle'])
admin.site.site_header="Gestion des commandes"