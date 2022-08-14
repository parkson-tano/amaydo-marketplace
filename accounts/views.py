from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView, View)
# Create your views here.

class UserProfileView(ListView):
	pass

class AccountBalanceView(ListView):
	pass

class MyAccountView(View):
	pass
