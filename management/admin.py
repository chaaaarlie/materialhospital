from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'description')

    list_filter = ('product_type',)


class ProposalDocumentsInline(admin.TabularInline):
    model = ProposalDocuments


class ProposalAdmin(admin.ModelAdmin):
    inlines = (ProposalDocumentsInline,)

    list_display = (
        'product',
        'image_tag',
        'supplier',
        'availability',
        'min_order_quantity',
        'payment_terms',
        'comments',
        'ce_certified',
        'fda_certified',
    )

    list_filter = ('proposal_type', 'supplier', 'product__product_type')

    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 height=100/>'.format(obj.picture.url))

    image_tag.short_description = 'Image'


admin.site.register(Supplier)
admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalDocuments)
admin.site.register(DocumentType)
