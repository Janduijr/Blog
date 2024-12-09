from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastrar_noticia,editar_noticia,listar_categoria,criar_categoria,editar_categoria,deletar_categoria

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('categoria/', listar_categoria, name='listar_categoria'),
    path('categoria/criar', criar_categoria, name='criar_categoria'),
    path('categoria/editar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categoria/deletar/<int:id>', deletar_categoria, name='deletar_categoria'),
    # Add your URL patterns here
]