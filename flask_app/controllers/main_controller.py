from flask_app import app
from flask import Flask, redirect, render_template, session, request
from flask_app.models.stocks import Stock
import yfinance as yf

@app.route('/')
def home():
    stock01 = yf.Ticker('^GSPC').info
    sp_500 =Stock(stock01)
    stock02 = yf.Ticker('^DJI').info
    dow =Stock(stock02)
    stock03 = yf.Ticker('^IXIC').info
    nasdaq =Stock(stock03)
    stock04 = yf.Ticker('^RUT').info
    russell =Stock(stock04)
    stock05 = yf.Ticker('CL=F').info
    crude_oil =Stock(stock05)
    stock06 = yf.Ticker('GC=F').info
    gold_stock =Stock(stock06)
    stock07 = yf.Ticker('SI=F').info
    silver_stock =Stock(stock07)

    stock_info = yf.Ticker('MSFT').info
    myStock = Stock(stock_info)
    stock_news = yf.Ticker('MSFT').news
    news = Stock.get_news(stock_news)
    return render_template('show_stock.html', stock = myStock, stories = news, sp500 = sp_500, dji = dow, nas = nasdaq, rus = russell, crude = crude_oil, gold = gold_stock, silver = silver_stock)

@app.route('/<ticker>')
def show_stock(ticker):
    stock01 = yf.Ticker('^GSPC').info
    sp_500 =Stock(stock01)
    stock02 = yf.Ticker('^DJI').info
    dow =Stock(stock02)
    stock03 = yf.Ticker('^IXIC').info
    nasdaq =Stock(stock03)
    stock04 = yf.Ticker('^RUT').info
    russell =Stock(stock04)
    stock05 = yf.Ticker('CL=F').info
    crude_oil =Stock(stock05)
    stock06 = yf.Ticker('GC=F').info
    gold_stock =Stock(stock06)
    stock07 = yf.Ticker('SI=F').info
    silver_stock =Stock(stock07)

    stock_info = yf.Ticker(ticker).info
    myStock = Stock(stock_info)
    stock_news = yf.Ticker(ticker).news
    news = Stock.get_news(stock_news)
    return render_template('show_stock.html', stock = myStock, stories = news, sp500 = sp_500, dji = dow, nas = nasdaq, rus = russell, crude = crude_oil, gold = gold_stock, silver = silver_stock)

@app.route('/search_ticker', methods=['POST'])
def search_ticker():
    # if not Stock.validate(request.form['ticker']):
    #     return redirect('/')
    ticker = request.form['ticker']
    return redirect(f"/{ticker}")

