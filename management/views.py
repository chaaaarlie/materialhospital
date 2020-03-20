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


class ProposalDetailView(DetailView):
    model = Proposal
    template_name = "management/proposal-detail.html"


def proposal_list(request):
    table = ProposalTable(Proposal.objects.all())

    return render(request, "management/index.html", {
        "table": table
    })


def proposalview(request):
    if request.method == "POST":
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ProposalForm()
    return render(request, 'management/proposal.html', {'form': form})


def edit(request, pk, template_name='management/edit.html'):
    proposal = get_object_or_404(Proposal, pk=pk)
    form = ProposalForm(request.POST or None, instance=proposal)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='management/confirm_delete.html'):
    proposal = get_object_or_404(Proposal, pk=pk)
    if request.method == 'POST':
        proposal.delete()
        return redirect('index')
    return render(request, template_name, {'object': proposal})
