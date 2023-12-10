from django.urls import path
from abrigo_animais.views import pagina_inicial, card_animais, contribuinte, pedido_adocao, pesquisar_animais, status, sobre, fale_conosco


urlpatterns = [
    path("", pagina_inicial, name='Abrigo_de_Animais'),
    path("animais/<int:id>", card_animais, name='Card_Animais'),
    path("contribuinte/", contribuinte, name='Contribuinte'),
    path("adoção/", pedido_adocao, name='Adoção'),
    path('pesquisar_animais/', pesquisar_animais, name="Pesquisar_Animais"),
    path('verificar_status/<int:pedido_id>/', status, name='Status'),
    path("sobre/", sobre, name='Sobre'),
    path("fale_conosco/", fale_conosco, name='Fale_Conosco')
] 