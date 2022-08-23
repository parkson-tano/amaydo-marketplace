from typing import List
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, PasswordResetForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView, View)
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


# Create your views here.

class IndexView(TemplateView):
	template_name = 'main/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		products = Product.objects.all() 
		context["products"] = products
		return context

class CartView(TemplateView):
	template_name = 'main/cart.html'

class ProductDetailView(TemplateView):
	template_name = 'main/product_detail.html'
	# model = Product
	# context_object_name = 'product'

class CategoryView(TemplateView):
	template_name = 'main/category.html'

class CheckOutView(TemplateView):
	template_name = 'main/checkout.html'	

class AddProductView(CreateView):
	template_name = 'main/add_product.html'
	form_class = ProductForm
	success_url = reverse_lazy('amydo:index')

	def form_valid(self, form):
		form.instance.owner = self.request.user
		p = form.save()
		images = self.request.FILES.getlist('more_images')
		for i in images:
			ProductImage.objects.create(product=p, image=i)
		return super().form_valid(form)

class OrderHistoryView(ListView):
	pass

class UserProductView(ListView):
	pass

class LogoutView(View):
	pass






# class EcoMixin(object):

# 	def dispatch(self, request, *args, **kwargs):

# 		cart_id = request.session.get('cart_id')
# 		if cart_id:
# 			cart_obj = Cart.objects.get(id=cart_id)
# 			if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
# 				cart_obj.UserProfile = request.user.UserProfile
# 				cart_obj.save()
# 		return  super().dispatch(request, *args, **kwargs)

# class IndexView(EcoMixin,TemplateView):
# 	template_name = 'index.html'
	
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['name'] = 'Parkson tano daniel'
# 		all_product = Product.objects.all().order_by('-id')
# 		paginator = Paginator(all_product, 8)
# 		page_number = self.request.GET.get('page')
# 		product_list = paginator.get_page(page_number)
# 		context['product_list'] = product_list
# 		return context

# class AboutView(EcoMixin,TemplateView):
# 	template_name = 'about.html'

# class ContactView(EcoMixin,TemplateView):
# 	template_name = 'contact.html'

# class AllProductsView(EcoMixin,TemplateView):
# 	template_name = 'allproduct.html'

# 	def get_context_data(self, **kwargs):
# 	    context = super().get_context_data(**kwargs)
# 	    context['allcategories'] = Category.objects.all().order_by('title')

# 	    return context

# class ProductDetailsView(EcoMixin, TemplateView):
# 	template_name = 'productdetails.html'
# 	def get_context_data(self, **kwargs):
# 	    context = super().get_context_data(**kwargs)
# 	    url_slug =  kwargs['slug']
# 	    product = Product.objects.get(slug=url_slug)
# 	    product.view_count += 1
# 	    product.save()
# 	    context['product'] = product
# 	    return context
	
# class AddToCartView(EcoMixin,TemplateView):
# 	template_name = 'addtocart.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 	    #get product id from requeted url
# 		product_id = self.kwargs['pro_id']
# 	    #get product
# 		product_obj = Product.objects.get(id=product_id)

# 		#check if cart exist
# 		cart_id = self.request.session.get('cart_id', None)

# 		if cart_id:
# 			cart_obj = Cart.objects.get(id=cart_id)
# 			this_product_in_cart = cart_obj.cartproduct_set.filter(product = product_obj)
# 			#items  in cart already
# 			if this_product_in_cart.exists():
# 				cartproduct = this_product_in_cart.last()
# 				cartproduct.quantity += 1
# 				cartproduct.subtotal += product_obj.selling_price
# 				cartproduct.rate = product_obj.selling_price
# 				cartproduct.save()
# 				cart_obj.total += product_obj.selling_price
# 				cart_obj.save()

# 			#new item 
# 			else:
# 				cartproduct = CartProduct.objects.create(
# 					cart = cart_obj, product=product_obj, subtotal=product_obj.selling_price, rate=product_obj.selling_price)
# 				cart_obj.total += product_obj.selling_price
# 				cart_obj.save()
# 		else:
# 			cart_obj = Cart.objects.create(total=0)
# 			self.request.session['cart_id'] = cart_obj.id
# 			cartproduct = CartProduct.objects.create(
# 					cart = cart_obj, product=product_obj, subtotal=product_obj.selling_price, rate=product_obj.selling_price)
# 			cart_obj.total += product_obj.selling_price
# 			cart_obj.save()
# 		#check if product already exist in cart
# 		return context

# class MyCartView(EcoMixin,TemplateView):
# 	template_name = 'mycart.html'

# 	def get_context_data(self, **kwargs):
# 	    context = super().get_context_data(**kwargs)
# 	    cart_id = self.request.session.get('cart_id', None)

# 	    if cart_id:
# 	    	cart = Cart.objects.get(id=cart_id)
# 	    else:
# 	    	cart = None
# 	    context['cart'] = cart
# 	    return context

# class ManageCartView(EcoMixin, View):
# 	def get(self, request, **kwargs):
# 		c_id = self.kwargs['c_id']
# 		action = request.GET.get('action')
# 		c_obj = CartProduct.objects.get(id=c_id)
# 		cart_obj = c_obj.cart
# 		cart_obj.save()

# 		if action == 'inc':
# 			c_obj.quantity += 1
# 			c_obj.subtotal += c_obj.rate
# 			c_obj.save()
# 			cart_obj.total += c_obj.rate
# 			cart_obj.save()

# 		elif action == 'dcr':
# 			if c_obj.quantity > 0:
# 				c_obj.quantity -= 1
# 				c_obj.subtotal -= c_obj.rate
# 				c_obj.save()
# 				cart_obj.total -= c_obj.rate
# 				cart_obj.save()
# 			else:
# 				c_obj.delete()	

# 		elif action == 'rmv':
# 			cart_obj.total -= c_obj.subtotal
# 			cart_obj.save()
# 			c_obj.delete()
# 		else:
# 			pass
# 		return redirect('amydo:mycart')

# class EmptyCartView(EcoMixin,View):

# 	def get(self, request, **kwargs):
# 		cart_id = request.session.get('cart_id', None)

# 		if cart_id:
# 			cart = Cart.objects.get(id=cart_id)
# 			cart.cartproduct_set.all().delete()
# 			cart.total = 0
# 			cart.save()

# 		return redirect('amydo:mycart')

# class CheckOutView(EcoMixin,CreateView):
# 	template_name = 'checkout.html'
# 	form_class = CheckOutForm
# 	success_url = reverse_lazy('amydo:index')
# 	#@method_decorator(csrf_exempt)

# 	def dispatch(self, request, *args, **kwargs):
# 		if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
# 			pass
# 		else:
# 			return redirect('/login/?next=/checkout/')

# 		return super().dispatch(request, *args, **kwargs)

# 	def form_valid(self, form):
# 		cart_id = self.request.session.get('cart_id')
# 		if cart_id:
# 			cart_obj = Cart.objects.get(id=cart_id)
# 			form.instance.cart = cart_obj
# 			form.instance.subtotal = cart_obj.total
# 			form.instance.discount = 0
# 			form.instance.total = cart_obj.total
# 			form.instance.order_status = 'Order_Recieved'
# 			del self.request.session['cart_id']
			
# 			pm =  form.cleaned_data.get('payment_method')
# 			order = form.save()
# 			if pm == 'Khalti':
# 				return redirect(reverse('amydo:paymentrequest') + "?o_id="+ str(order.id))
# 		else:
# 			return redirect('amydo:index')

# 		return super().form_valid(form)

# 	def get_context_data(self, **kwargs):
# 	    context = super().get_context_data(**kwargs)
# 	    cart_id = self.request.session.get('cart_id', None)

# 	    if cart_id:
# 	    	cart_obj = Cart.objects.get(id=cart_id)

# 	    else:
# 	    	cart_obj = None

# 	    context['cart'] = cart_obj

# 	    return context

# class UserProfileLogoutView(View):
	
# 	def get(self, request):
# 		logout(request)
# 		return redirect('amydo:index')

# class UserProfileView(TemplateView):
# 	template_name = 'UserProfileprofile.html'


# 	def dispatch(self, request, *args, **kwargs):
# 		if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
# 			pass
# 		else:
# 			return redirect('/login/?next=/profile/')

# 		return super().dispatch(request, *args, **kwargs)

# 	def get_context_data(self, **kwargs):
# 	    context = super().get_context_data(**kwargs)
# 	    UserProfile = self.request.user.UserProfile
# 	    context['UserProfile'] = UserProfile	

# 	    orders = Order.objects.filter(cart__UserProfile=UserProfile).order_by('-id')
# 	    context['order'] = orders

# 	    return context
		
# class UserProfileOrderDetailView(DetailView):
# 	template_name = 'UserProfileorderdetail.html'
# 	model = Order
# 	context_object_name = 'ord_obj'

# 	def dispatch(self, request, *args, **kwargs):
# 		if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
# 			order_id = self.kwargs['pk']
# 			order = Order.objects.get(id=order_id)

# 			action = request.GET.get('action')
# 			ord_obj = Order.objects.get(id=order_id)
# 			order_obj = ord_obj.cart
# 			if action == 'rmv':
# 				order_obj.save()
# 				order_obj.delete()
# 				return redirect('amydo:UserProfileprofile')
# 			else:
# 				pass

# 			if request.user.UserProfile != order.cart.UserProfile:
# 				return redirect('amydo:UserProfileprofile')
# 			else:
# 				pass
# 		else:
# 			return redirect('/login/?next=/profile/')


# 		return super().dispatch(request, *args, **kwargs)

		
# class SearchView(TemplateView):
# 	template_name = 'search.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		kw = self.request.GET['keyword']
# 		results = Product.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw))
# 		context['results'] = results 
# 		return context

