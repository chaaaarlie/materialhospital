import django_tables2 as tables
from .models import Proposal
from django.utils.html import format_html


class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<a href={url} target="_blank"><img src="{url}" width=100 height=100 /><a/>', url=value)


class ProposalTable(tables.Table):
    picture = ImageColumn()

    class Meta:
        model = Proposal
        attrs = {"align": "center"}
