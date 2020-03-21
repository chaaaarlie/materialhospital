from django.db import models
from django_countries.fields import CountryField


class Supplier(models.Model):
    name = models.CharField(max_length=32
                            , help_text="Nome do Fornecedor")

    email = models.EmailField(max_length=254
                              , help_text="Email do fornecedor"
                              , blank=True)

    phone = models.CharField(max_length=32
                              , help_text="Telefone do Fornecedor"
                              , blank=True)

    lead = models.CharField(max_length=32
                            , help_text="Identificação do lead"
                            , blank=True)

    origin = CountryField(blank_label='(selecionar pais)'
                          , blank=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):

    type = models.CharField(max_length=32
                            , choices=[('E', 'Equipamento Protecao Individual'), ('V', 'Ventilador'), ('T', 'Kit Teste')]
                            , help_text='Tipo de Produto', blank=True, default=None)

    product_type = models.CharField(max_length=32, help_text="Tipo de Produto", blank=True, default=None)

    designation = models.CharField(max_length=128, help_text="Designação do Produto", blank=True,)

    def __str__(self):
        return self.product_type


class Product(models.Model):

    product_type = models.ForeignKey(ProductType
                                     , on_delete=models.DO_NOTHING
                                     , blank=True
                                     , default=None)

    title = models.CharField(max_length=64
                             , help_text="Nome do Produto")

    model = models.CharField(max_length=64
                             , help_text="Modelo do Produto"
                             , blank=True)

    description = models.CharField(max_length=128
                                   , help_text="Descrição do produto"
                                   , blank=True)

    def __str__(self):
        return self.title


class Proposal(models.Model):

    proposal_type = models.CharField(max_length=24
                                     , choices=[('D', 'Doação'), ('C', 'Comercial')]
                                     , help_text="Tipo de Proposta"
                                     , blank=True
                                     , default=None)

    supplier = models.ForeignKey(Supplier
                                 , help_text="Nome do Fornecedor"
                                 , on_delete=models.DO_NOTHING
                                 , blank=True
                                 , default=None)

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING
                                , blank=True
                                , default=None)

    availability = models.IntegerField(help_text="Inserir valor total sem abreviatura")

    min_order_quantity = models.IntegerField(help_text="Inserir valor total sem abreviatura"
                                             , blank=True)

    unit_price = models.DecimalField(decimal_places=2
                                     , max_digits=10
                                     , blank=True)

    picture = models.ImageField(upload_to='./uploads/images/')

    payment_terms = models.CharField(max_length=128
                                     , help_text='Termos de pagamento'
                                     , blank=True)

    comments = models.TextField(max_length=1024, help_text="Notas/ Comentários", blank=True)

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
    proposal = models.ForeignKey(Proposal, on_delete=models.DO_NOTHING)

    file_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING)

    file = models.FileField(upload_to='./uploads/files/')

    def __str__(self):
        return self.proposal.product.title
