from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name='portfolio/index.html'
    queryset = ''

    def get(self, request):
        return render(request, 'portfolio/index.html')