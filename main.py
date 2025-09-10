import streamlit as st
import requests
import yfinance as yf
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt

# === Config ===
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
sentiment_model = pipeline("sentiment-analysis")

# === 1. Get latest news from Google News API ===
def get_news(stock_symbol):
    url = f"https://newsapi.org/v2/everything?q={stock_symbol}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "articles" in data:
        headlines = [article["title"] for article in data["articles"][:5]]
        return headlines
    return []

# === 2. Get stock price ===
def get_stock_price(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(period="100d")
    return data

# === 3. Analyze sentiment ===
def analyze_sentiment(headlines):
    if not headlines:
        return 0, []
    results = sentiment_model(headlines)
    scores = []
    for r in results:
        score = r['score'] if r['label'] == 'POSITIVE' else -r['score']
        scores.append(score)
    avg_score = sum(scores) / len(scores)
    return avg_score, list(zip(headlines, scores))

# === 4. Streamlit Dashboard ===
def main():
    st.title("📈 Stock Market Research Agent")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, INFY.BO)", "AAPL")

    if st.button("Analyze"):
        # Fetch stock data
        st.subheader(f"🔹 Stock Price for {stock_symbol}")
        price_data = get_stock_price(stock_symbol)
        st.line_chart(price_data["Close"])
        latest_price = price_data["Close"].iloc[-1]
        st.write(f"**Latest Price:** ${latest_price:.2f}")

        # Fetch news + sentiment
        st.subheader("📰 Latest News Headlines")
        headlines = get_news(stock_symbol)
        if headlines:
            avg_sentiment, detailed = analyze_sentiment(headlines)

            for headline, score in detailed:
                sentiment_label = "📈 Bullish" if score > 0 else "📉 Bearish"
                st.write(f"- {headline} ({sentiment_label}, Score: {score:.2f})")

            st.subheader("📊 Overall Sentiment")
            st.metric("Sentiment Score", f"{avg_sentiment:.2f}",
                      "Bullish" if avg_sentiment > 0 else "Bearish")
        else:
            st.warning("No news found for this stock.")

if __name__ == "__main__":
    main()
