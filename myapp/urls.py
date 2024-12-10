from django.urls import path
import myapp.views as vw

urlpatterns = [
    path('', vw.inicio, name="inicio"),
    path('componentes/', vw.componentes, name="componentes"),
    path('colaboradores/', vw.colaboradores, name="colaboradores"),
    path('sedes/', vw.sedes, name="sedes"),
    path('componente-formulario/', vw.formulario_componentes_api, name="componentes-formulario"),
    path('sede-formulario/', vw.formulario_sede_api, name="sede-formulario"),
    path('colaborador-formulario/', vw.formulario_colaborador_api, name="colaborador-formulario"),

]