from rest_framework import serializers
from .models import product_info

class product_infoSerializer(serializers.ModelSerializer):

	class Meta:
		model=product_info
		#fields=('product title', 'price', 'image', 'description', 'category')
		fields = "__all__"
