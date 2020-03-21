from django.shortcuts import render, redirect, get_object_or_404
from .models import Proposal
from .forms import ProposalForm
from .tables import ProposalTable
from .filters import ProposalFilter
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableView

# Create your views here.


class IndexView(SingleTableView):
    model = Proposal
    template_name = "management/index.html"
    table_class = ProposalTable

    def index(self, request):

        return render(request, self.template_name, context=self.table)

