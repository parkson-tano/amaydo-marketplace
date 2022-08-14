from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField
from accounts.models import *
# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='title', unique=True)

	def __str__(self):
		return self.title

class Product(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200)
	category =models.ForeignKey(Category, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/')
	price = models.FloatField(default=0)
	marked_price = models.FloatField(null=True, blank=True)
	description = models.TextField()
	quantity = models.IntegerField(default=0)
	town = models.CharField(max_length=256, null=True, blank=True)
	warranty = models.CharField(max_length=100, null=True, blank = True)
	return_policy = models.CharField(max_length=100, null=True, blank=True)
	contact = models.BigIntegerField(null=True, blank=True)
	view_count = models.PositiveIntegerField(default=0)
	date_created = models.DateTimeField(default=now)
	free_delivery = models.BooleanField(default=False)
	delivery_fee = models.FloatField(null=True, blank=True)
	slug = AutoSlugField(
		populate_from=lambda instance: instance.name,
                         unique_with=['owner__userprofile__id', 'date_created'],
                         slugify=lambda value: value.replace(' ','-')
	)


	def __str__(self):
		return self.name

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products.image/')

	def __str__(self):
		return self.product.name
	

class  Cart(models.Model):
	customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
	total = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Cart: {str(self.id)}"
class CartProduct(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	rate = models.PositiveIntegerField(default=1)
	quantity = models.PositiveIntegerField(default=1)
	subtotal = models.PositiveIntegerField(default=1)

	def __str__(self):
		return f"Cart: {str(self.cart.id)} CartProduct {str(self.id)}"

ORDER_STATUS = (
		('Order Recieved', 'Order Recieved'),
		('Order Processing',  'Order Processing'),
		('On the way', 'On the way'),
		('Order Complete', 'Order Complete'),
		('Order Cancel', 'Order Cancel'),
	)

METHOD = (
	("Cash On Delivery", "Cash On Delivery"),
	('Mobile Money', 'Mobile Money'),

)
class Order(models.Model):
	cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
	ordered_by = models.CharField(max_length=200)
	shipping_address  = models.CharField(max_length=200)
	mobile = models.CharField(max_length=10)
	email = models.EmailField(null=True, blank=True)
	subtotal = models.PositiveIntegerField()
	discount = models.PositiveIntegerField()
	total = models.PositiveIntegerField()
	order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Order Recieved')
	date_created = models.DateTimeField(auto_now_add=True)
	payment_method = models.CharField(max_length = 20, choices=METHOD, default='Cash On Delivery')
	payment_completed = models.BooleanField(default=False, null=True, blank=True)

	def __str__(self):
		return f"Order: {str(self.id)}"