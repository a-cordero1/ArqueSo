from ..models import Solicitud

def get_solicitudes():
	solicitudes = Solicitud.objects.all()
	return solicitudes

def get_solicitud(sol_pk):
	solicitud = Solicitud.objects.get(pk=sol_pk)
	return solicitud

def update_solicitud(sol_pk, new_sol):
    solicitud = get_solicitud(sol_pk)
    solicitud.tipo = new_sol["tipo"]
    solicitud.fecha = new_sol["fecha"]
    solicitud.save()
    return solicitud

def create_solicitud(sol):
    solicitud = Solicitud(tipo=sol["tipo"], fecha=sol["fecha"])
    solicitud.save()
    return solicitud