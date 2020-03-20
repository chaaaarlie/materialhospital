from django.contrib import admin

# Register your models here.
from .models import Supplier, Proposal, ProductType, Product, Contact, ProposalDocuments, ProposalState, Donation, DocumentType

admin.site.register(Supplier)
admin.site.register(Contact)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Proposal)
admin.site.register(ProposalDocuments)
admin.site.register(ProposalState)
admin.site.register(Donation)
admin.site.register(DocumentType)