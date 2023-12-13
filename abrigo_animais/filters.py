import django_filters
from django.db.models import Q
from animais.models import CadastroAnimal
from unidecode import unidecode

class AnimalFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = CadastroAnimal
        fields = '__all__'
        exclude = ['foto']

    def filter_search(self, queryset, _, value):
        if not value:
            return queryset

        value = unidecode(value.lower())
        q_objects = [
            Q(**{f'{field}__icontains': value}) 
            for field in ['nome', 'espécie', 'idade', 'raça', 'histórico_de_saúde']
        ]

        q_object = Q()
        for obj in q_objects:
            q_object |= obj

        return queryset.filter(q_object)