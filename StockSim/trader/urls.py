from django.urls import path

from . import views

app_name = 'trader'
urlpatterns=[
    path('', views.MarketView.as_view(), name='lookup'),
    path('trade/', views.TradeView.as_view(), name='trade'),
]