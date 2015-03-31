from django import forms
from .models import Plato , Menu


class PanelDesayunosForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(PanelDesayunosForm, self).__init__(*args, **kwargs)
		#le doy el widget de multiple seleccionador y le paso el queryset
		self.fields['platos'].widget= forms.CheckboxSelectMultiple()
		self.fields['platos'].queryset= Plato.objects.all()
		self.fields['platos'].help_text=""
		
		# | se usa para "sumar" dos querysets

	class Meta:
		model = Menu
		fields = ( 'platos' ,)


class PanelAlmuerzosForm(forms.ModelForm):

	def __init__ (self , *args , **kwargs):
		super(PanelAlmuerzosForm, self).__init__(*args , **kwargs)

		self.fields['platos'].widget=forms.CheckboxSelectMultiple()
		self.fields['platos'].queryset = Plato.objects.all()
		self.fields['platos'].help_text=''

	class Meta:
		model = Menu
		fields = ('platos' ,) 

		


	