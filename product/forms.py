from django import forms
from  .models import Order, Product
from django.contrib.auth.models import User

class CheckOutForm(forms.ModelForm):
	class Meta:
		model = Order 
		fields = ['ordered_by', 'shipping_address',  'mobile', 'email', 'payment_method']


class ProductForm(forms.ModelForm):

	more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
		'class': 'form-control',
		'multiple': True
	}))
	class Meta:
		model = Product
		fields = ['name', 'price', 'marked_price', 'category', 'description','quantity', 'contact',
		 'town', 'warranty', 'return_policy', 'free_delivery', 'delivery_fee','image']

		widgets = {
			"name": forms.TextInput(attrs= { 
				'placeholder': 'Enter the Product Title'
			}),
			"price": forms.NumberInput(attrs= { 
				'placeholder': 'Enter the Marked_Price'
			}),
			"marked_price": forms.NumberInput(attrs= { 
				'placeholder': 'Enter the Selling Price'
			}),
			"description": forms.Textarea(attrs= { 
			'placeholder': 'Enter the Product Description',
			'rows': 5
		
			}),
			"warranty": forms.TextInput(attrs= { 
				'placeholder': 'Enter the Product Warranty'
			}),
				"return_policy": forms.TextInput(attrs= { 
				'placeholder': 'Enter the Product return policy'
			}),

		}
		labels = {
			'name': 'Product Title',
		}