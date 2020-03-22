from django.db import models
from django_countries.fields import CountryField


class Supplier(models.Model):
    name = models.CharField(max_length=32
                            , help_text="Nome do Fornecedor")

    email = models.EmailField(max_length=254
                              , help_text="Email do fornecedor"
                              , blank=True, null=True)

    phone = models.CharField(max_length=32
                              , help_text="Telefone do Fornecedor"
                              , blank=True, null=True)

    lead = models.CharField(max_length=32
                            , help_text="Identificação do lead"
                            , blank=True, null=True)

    origin = CountryField(blank_label='(selecionar pais)'
                          , blank=True, null=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):

    type = models.CharField(max_length=32
                            , choices=[('E', 'Equipamento Protecao Individual'), ('V', 'Ventilador'), ('T', 'Kit Teste')]
                            , help_text='Tipo de Produto', blank=True, default=None, null=True)

    product_type = models.CharField(max_length=32, help_text="Tipo de Produto", blank=True, null=True, default=None)

    designation = models.CharField(max_length=128, help_text="Designação do Produto", blank=True, null=True)

    def __str__(self):
        return self.product_type


class Product(models.Model):

    product_type = models.ForeignKey(ProductType
                                     , on_delete=models.SET_NULL
                                     , blank=True
                                     , default=None
                                     , null=True)

    title = models.CharField(max_length=64
                             , help_text="Nome do Produto")

    model = models.CharField(max_length=64
                             , help_text="Modelo do Produto"
                             , blank=True, null=True)

    description = models.CharField(max_length=128
                                   , help_text="Descrição do produto"
                                   , blank=True, null=True)

    def __str__(self):
        return self.title


class Proposal(models.Model):

    proposal_type = models.CharField(max_length=24
                                     , choices=[('D', 'Doação'), ('C', 'Comercial')]
                                     , help_text="Tipo de Proposta"
                                     , blank=True, null=True
                                     , default=None)

    supplier = models.ForeignKey(Supplier
                                 , help_text="Nome do Fornecedor"
                                 , on_delete=models.SET_NULL
                                 , blank=True
                                 , default=None
                                 , null=True)

    product = models.ForeignKey(Product, on_delete=models.PROTECT, default=None)

    availability = models.IntegerField(help_text="Inserir valor total sem abreviatura")

    min_order_quantity = models.IntegerField(help_text="Inserir valor total sem abreviatura"
                                             , blank=True, null=True)

    unit_price = models.DecimalField(decimal_places=2
                                     , max_digits=10
                                     , blank=True, null=True)

    picture = models.ImageField(upload_to='images/')

    payment_terms = models.CharField(max_length=128
                                     , help_text='Termos de pagamento'
                                     , blank=True, null=True)

    comments = models.TextField(max_length=1024, help_text="Notas/ Comentários", blank=True, null=True)

    ce_certified = models.NullBooleanField()

    fda_certified = models.NullBooleanField()

    def __str__(self):
        return '{} from {}'.format(self.product, self.supplier)


class Order(models.Model):

    STATUS_CHOICES = (
        ('P', 'Prospective'),
        ('O', 'Ordered'),
        ('A', 'Arrived'),
        ('C', 'Cancelled'),
    )
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    proposal = models.ForeignKey('Proposal', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return '{} {}, {}'.format(self.quantity, self.product, self.proposal)


class DocumentType(models.Model):
    file_type = models.CharField(max_length=64
                                 , help_text='Tipo de Documento')
    description = models.CharField(max_length=256
                                   , help_text='Descrição do Documento')

    def __str__(self):
        return self.file_type


class ProposalDocuments(models.Model):
    proposal = models.ForeignKey(Proposal
                                 , on_delete=models.CASCADE)

    file_type = models.ForeignKey(DocumentType
                                  , on_delete=models.SET_NULL
                                  , null=True
                                  , blank=True
                                  , default=None)

    file = models.FileField(upload_to='files/')

    def __str__(self):
        return '{} - {}'.format(self.file_type, self.proposal)

    class Meta:
        verbose_name = 'Proposal Document'
        verbose_name_plural = 'Proposal Documents'
