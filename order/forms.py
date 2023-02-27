from django.forms import ModelForm
from order.models import Order


class OderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'plated_end_at')

