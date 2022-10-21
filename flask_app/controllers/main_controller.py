from flask_app import app
from flask import Flask, redirect, render_template, session, request
from flask_app.models.stocks import Stock
import yfinance as yf

@app.route('/')
def home():
    stock_info = yf.Ticker('MSFT').info
    myStock = Stock(stock_info)
    stock_news = yf.Ticker('MSFT').news
    news = Stock.get_news(stock_news)
    return render_template('show_stock.html', stock = myStock, stories = news)

@app.route('/<ticker>')
def show_stock(ticker):
    stock_info = yf.Ticker(ticker).info
    myStock = Stock(stock_info)
    stock_news = yf.Ticker(ticker).news
    news = Stock.get_news(stock_news)
    
    return render_template('show_stock.html', stock = myStock, stories = news)

@app.route('/search_ticker', methods=['POST'])
def search_ticker():
    # if not Stock.validate(request.form['ticker']):
    #     return redirect('/')
    ticker = request.form['ticker']
    return redirect(f"/{ticker}")

