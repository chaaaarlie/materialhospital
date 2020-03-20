import django_filters
from .models import Proposal


class ProposalFilter(django_filters.FilterSet):
    class Meta:
        model = Proposal
        fields = ['supplier', 'product', 'payment_terms']
