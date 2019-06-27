from django import forms

from .widgets import AjaxInputWidget


class SearchTicket(forms.Form):
    departure = forms.CharField(widget=AjaxInputWidget('api/city_ajax',
                                            attrs={'class': 'inline right-margin'}),
                                        label='Откуда')
    destination = forms.CharField(widget=AjaxInputWidget('api/city_ajax',
                                            attrs={'class': 'inline right-margin'}),
                                        label='Куда')
    date_departure = forms.DateField(widget=forms.DateTimeInput(
                                            attrs={'class': 'inline right-margin', 'type': 'date'}),
                                        label='Когда')
