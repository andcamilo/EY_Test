from django.urls import path
from django.conf.urls import url, include
from app import views 


urlpatterns = [
    path(
        '<persona_id>/',
        views.index,
        name='index'
    ),

    path(
        route='',
        view=views.CreatePersonaView.as_view(),
        name='persona_add'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

      
    



