from django.forms import ModelForm
from .models import product_info

# Create your models here.
class product_form(ModelForm):
	# title = forms.CharField(max_length=200)
	# price = forms.DecimalField(max_digits=10, decimal_places=2)
	# image = forms.FileField()
	# description = forms.CharField(max_length=500)
	# category = forms.CharField(max_length=10)
	class Meta:
		model=product_info
		fields='__all__'

	def __str__(self):
		return self.title
