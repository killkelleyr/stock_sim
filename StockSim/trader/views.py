from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
import environ
#from Robinhood import Robinhood
from pyrh import Robinhood

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users
from accounts.models import Account

@method_decorator(login_required, name='dispatch')
class MarketView(generic.ListView):
	template_name='trader/lookup.html'
	queryset = ''

	def get(self, request):
		#return HttpResponse(request.user.id)
		#env = environ.Env(DEBUG=(bool, False))
		# reading .env file
		#environ.Env.read_env()
		currentUser = Account.objects.get(user=request.user)
		my_trader = Robinhood()
		my_trader.login(username=currentUser.rhoodID, password=currentUser.rhoodPWD, qr_code=currentUser.rhQ)
		data=my_trader.portfolios()
		my_trader.logout()
		return HttpResponse(data)
		context={}
		return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class TradeView(generic.ListView):
    template_name='trader/trade.html'
    queryset = ''