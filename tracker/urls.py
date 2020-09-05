from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:p_id>/', views.detail, name='detail'),
    path('<int:p_id>/results/', views.results, name='results'),
    path('<int:p_id>/vote/', views.vote, name='vote'),
    path('game/<str:name>', views.game, name='game'),
]