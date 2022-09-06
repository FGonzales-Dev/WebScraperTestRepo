from django.urls import path
from core import historicalData, scraperVersionTwo, views

urlpatterns = [
    path('stock/<data_param>/', views.home, name='home'),
    path('history', views.stockhistory, name='home'),
    path('income_statement', views.stock_income_statement, name='home'),
    path('cash_flow', views.stock_cash_flow, name='home'),
    # path('stock_history', historicalData.stock_history, name='home'),
    
    path('stock_history_all', historicalData.stock_history_all, name='home'),
    path('stock_history_key_ratio', historicalData.stock_history_key_ratio, name='home'),
    path('scrape', historicalData.scrape, name='scrape'),
    path('valuation', historicalData.scrape_valuation, name='valuation'),
    path('dividends', historicalData.scrape_dividends, name='dividends'),
    path('performance', historicalData.scrape_operating_performance, name='performance'),
    path('stock_history_key_ratio_json', historicalData.stock_history_key_ratio_json, name='home'),
    ######TEST FOR JSON#######
      path('stock_history_json', historicalData.stock_history_json, name='home')
    ######TEST FOR JSON#######
]


#http://127.0.0.1:8000/stock_history_json?ticker=aapl&market=XNAS&type=is