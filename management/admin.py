from admin_totals.admin import ModelAdminTotals
from django.contrib import admin

# Register your models here.
from django.db.models import Sum, Min
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import format_html
from django_countries.filters import CountryFilter

from .models import *


class OrderAdmin(ModelAdminTotals):
    list_display = (
        'product',
        'proposal',
        'quantity',
        'created',
        'updated',
        'status',
    )

    list_editable = ('status',)

    list_filter = ('product__product_type', 'product', 'status', 'proposal__supplier')

    list_totals = (('quantity', Sum),)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'description')

    list_filter = ('product_type',)


class ProposalDocumentsInline(admin.TabularInline):
    model = ProposalDocuments


class ProposalAdmin(ModelAdminTotals):
    actions = ['order']
    inlines = (ProposalDocumentsInline,)

    list_display = (
        'product',
        'proposal_type',
        'image_tag',
        'supplier',
        'availability',
        'min_order_quantity',
        'unit_price',
        'payment_terms',
        'comments',
        'ce_certified',
        'fda_certified',
    )

    list_editable = ('availability', 'unit_price')

    list_totals = (('availability', Sum), ('min_order_quantity', Min))

    list_filter = ('proposal_type', 'product__product_type', 'product', 'supplier')

    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 height=100/>'.format(obj.picture.url))

    image_tag.short_description = 'Image'

    def order(self, request, queryset):
        if 'apply' in request.POST:
            for proposal in queryset:
                quantity = request.POST[str(proposal.id)]
                Order.objects.create(proposal=proposal, product=proposal.product, quantity=quantity, status='O')
            self.message_user(request,
                              "Ordered {} product(s)".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        return render(request, 'admin/order_intermediate.html', context={'orders': queryset})
    order.short_description = 'Encomendar'


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'lead', 'origin']
    list_filter = [('origin', CountryFilter)]


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalDocuments)
admin.site.register(DocumentType)
