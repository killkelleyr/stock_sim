from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
import os, base64
import environ
#from Robinhood import Robinhood
from pyrh import Robinhood

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users

@method_decorator(login_required, name='dispatch')
class MarketView(generic.ListView):
	template_name='trader/lookup.html'
	queryset = ''

	def get(self, request):
		env = environ.Env(DEBUG=(bool, False))
		# reading .env file
		environ.Env.read_env()
		my_trader = Robinhood()
		my_trader.login(username=env('rhu'), password=base64.b64decode(env('rhp')).decode('utf-8'), qr_code=env('rhq'))
		my_trader.logout()
		context={}
		return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class TradeView(generic.ListView):
    template_name='trader/trade.html'
    queryset = ''