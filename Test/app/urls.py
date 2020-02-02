from django.urls import path
from django.conf.urls import url, include
from app import views 


urlpatterns = [

    path (
        route='',
        view= views.CreatePersonaView.as_view(),
        name='persona_add'

    ),

    path (
        route='list',
        view= views.ListPersonaView.as_view(),
        name='list_persona'
    ),
   
]
      
    



