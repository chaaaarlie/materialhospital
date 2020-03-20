from django.db import models
from django_countries.fields import CountryField


class Supplier(models.Model):
    name = models.CharField(max_length=32
                            , help_text="Nome do Fornecedor")
    email = models.EmailField(max_length=254
                              , help_text="Contacto do Fornecedor (ie, email, telefone)"
                              , blank=True)
    lead = models.CharField(max_length=32
                            , help_text="Identificação do lead"
                            , blank=True)
    origin = CountryField(blank_label='(selecionar pais)'
                          , blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    supplier = models.ForeignKey(Supplier
                                 , on_delete=models.DO_NOTHING)


class ProductType(models.Model):
    type = models.CharField(max_length=32
                            , help_text="Tipo de Produto")
    designation = models.CharField(max_length=128
                                   , help_text="Designação do Produto")

    def __str__(self):
        return self.type


class Product(models.Model):
    product_type = models.ForeignKey(ProductType
                                     , on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=32
                             , help_text="Nome do Produto")
    description = models.CharField(max_length=32
                                   , help_text="Descrição do produto"
                                   , blank=True)
    model = models.CharField(max_length=32
                             , help_text="Modelo do Produto"
                             , blank=True)
    make = models.CharField(max_length=32
                            , help_text="Marca do Produto"
                            , blank=True)

    def __str__(self):
        return self.title


class Proposal(models.Model):
    supplier = models.ForeignKey(Supplier
                                 , help_text="Nome do Fornecedor"
                                 , on_delete=models.DO_NOTHING
                                 , blank=True
                                 , default=None)
    product = models.ForeignKey(Product
                                , on_delete=models.DO_NOTHING)
    availability = models.IntegerField()
    min_order_quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2
                                     , max_digits=10)
    picture = models.ImageField(upload_to='./uploads/images/')
    payment_terms = models.CharField(max_length=128
                                     , help_text='Termos de pagamento'
                                     , blank=True)
    ce_certified = models.NullBooleanField()
    fda_certified = models.NullBooleanField()

    def __str__(self):
        return self.product.title


class DocumentType(models.Model):
    file_type = models.CharField(max_length=64
                                 , help_text='Tipo de Documento')
    description = models.CharField(max_length=256
                                   , help_text='Descrição do Documento')

    def __str__(self):
        return self.file_type


class ProposalDocuments(models.Model):
    proposal = models.ForeignKey(Proposal
                                 , on_delete=models.DO_NOTHING)
    file_type = models.ForeignKey(DocumentType
                                  , on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='./uploads/files/')

    def __str__(self):
        return self.proposal.product.title


class ProposalState(models.Model):
    proposal = models.ForeignKey(Proposal
                                 , on_delete=models.DO_NOTHING)


class Donation(models.Model):
    product = models.ForeignKey(Product
                                , on_delete=models.DO_NOTHING)
    availability = models.IntegerField()

