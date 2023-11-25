from django.urls import path
from animais.views import cadastro_animal
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('cadastro_animal/', cadastro_animal, name='cadastro_animal'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)