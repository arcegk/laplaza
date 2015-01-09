from django import forms
from .models import Plato , Menu


class PanelForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(PanelForm, self).__init__(*args, **kwargs)
		#le doy el widget de multiple seleccionador y le paso el queryset
		self.fields['platos'].widget= forms.CheckboxSelectMultiple()
		self.fields['platos'].queryset= Plato.objects.order_by('tipo')

	class Meta:
		model = Menu
		fields = ( 'platos' , )

		


	