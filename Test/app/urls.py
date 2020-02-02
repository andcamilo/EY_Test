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


    path(
        route='update_persona/<int:id>/', 
        view=views.UpdatePersonalView.as_view(),
        name='update_persona'
    ), 

    path(
        route='detail_persona/<int:id>/',
        view=views.DetailPersonaView.as_view(),
        name='detail_persona'
    ),

    
]
      
    



