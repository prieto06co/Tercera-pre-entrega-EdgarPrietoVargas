BackEnd Django - Tercera pre-entrega

Autor: Edgar Armando Prieto Vargas
Fecha: 09/12/2024
Versión: 20241209

Estructura del proyecto:

miSitio/
│
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── componentes.html
│   │       ├── colaboradores.html
│   │       ├── sedes.html
│   │       └── forms/
│   │           ├── componente-formulario.html
│   │           ├── colaborador-formulario.html
│   │           └── sede-formulario.html
│   └── urls.py
│    
│
├── db.sqlite3
├── manage.py
└── readme.txt

# My Django App

## Cómo Probar el Proyecto
1. Clonar el repositorio:
   ```bash
   git clone <link-del-repositorio>
   cd miSitio
2. Instalar paquete Django:
	pip install django
3. Ejecutar Migraciones y creación DB
	python manage.py makemigrations
	python manage.py migrate
4. Ejecutar Servidor:
	python manage.py runserver
	
Funcionalidades
Home: Página de inicio (http://127.0.0.1:8000/).
Componentes: Pagina con listado de Componentes (http://127.0.0.1:8000/componentes/).
Colaboradores: Pagina con listado de Colaboradores (http://127.0.0.1:8000/colaboradores/).
Sedes: Pagina con listado de Sedes (http://127.0.0.1:8000/sedes/).

Agregar Componentes: Formulario para agregar Componentes (http://127.0.0.1:8000/componente-formulario/).
Agregar Colaboradores: Formulario para agregar Colaboradores (http://127.0.0.1:8000/colaborador-formulario/).
Agregar Sedes: Formulario para agregar Sedes (http://127.0.0.1:8000/sede-formulario/).
