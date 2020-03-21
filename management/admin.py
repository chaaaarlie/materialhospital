from django.contrib import admin

# Register your models here.
from .models import Supplier, Proposal, ProductType, Product,  ProposalDocuments, DocumentType

admin.site.register(Supplier)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Proposal)
admin.site.register(ProposalDocuments)
admin.site.register(DocumentType)