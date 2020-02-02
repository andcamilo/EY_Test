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
    route='email',
    view= views.CreateEmailView.as_view(),
    name='email_add'

    ),

    path (
        route='list',
        view= views.ListPersonaView.as_view(),
        name='list_persona'
    ),

    path(
        route='persona_delete/<int:id>/', 
        view=views.DeletePersonaView.as_view(),
        name='persona_delete'
),
   
]
      
    



