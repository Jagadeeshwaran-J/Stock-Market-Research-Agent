# 📈 Stock Market Research Agent
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-Stock%20Data-purple?logo=yahoo)](https://finance.yahoo.com/)
[![NewsAPI](https://img.shields.io/badge/NewsAPI-Headlines-orange?logo=news)](https://newsapi.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Sentiment%20Models-yellow?logo=huggingface)](https://huggingface.co/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)](https://streamlit.io/)

A powerful Streamlit web application that combines real-time stock data with AI-powered news sentiment analysis to help investors make informed decisions.

## 🚀 Features

- **Real-time Stock Data**: Fetch and visualize stock prices using Yahoo Finance
- **News Integration**: Get latest news headlines from NewsAPI
- **AI Sentiment Analysis**: Analyze news sentiment using Hugging Face transformers
- **Interactive Dashboard**: Clean and intuitive Streamlit interface
- **Visual Analytics**: Price charts and sentiment scoring
- **Multi-market Support**: Works with US stocks, Indian stocks (NSE/BSE), and more

## 📊 What It Does

1. **Stock Price Analysis**: Displays 150-day price history with interactive charts
2. **News Aggregation**: Fetches the 5 most recent news articles for any stock
3. **Sentiment Scoring**: Uses AI to analyze whether news is bullish (📈) or bearish (📉)
4. **Overall Assessment**: Provides an aggregated sentiment score to gauge market mood

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- NewsAPI key (free from [newsapi.org](https://newsapi.org/))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jagadeeshwaran-J/Stock-Market-Research-Agent.git
   cd Stock-Market-Research-Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   
   Replace the API key in the code:
   ```python
   NEWS_API_KEY = "your_newsapi_key_here"
   ```
   
   Or better yet, use environment variables:
   ```python
   import os
   NEWS_API_KEY = os.getenv("NEWS_API_KEY", "your_default_key")
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🎯 Usage

1. **Launch the app**: Run `streamlit run app.py`
2. **Enter stock symbol**: Type any valid stock symbol (e.g., AAPL, TSLA, GOOGL, INFY.BO)
3. **Click Analyze**: Get comprehensive analysis including:
   - Stock price chart (150-day history)
   - Latest closing price
   - Recent news headlines with sentiment scores
   - Overall sentiment assessment

## 📈 Supported Stock Symbols

- **US Stocks**: AAPL, TSLA, GOOGL, MSFT, AMZN, etc.
- **Indian Stocks**: INFY.BO, TCS.BO, RELIANCE.BO, etc.
- **International**: Many global exchanges supported by Yahoo Finance

## 🧠 AI Model

Uses Hugging Face's pre-trained sentiment analysis model for accurate news sentiment classification:
- **Positive sentiment**: Bullish indicator (📈)
- **Negative sentiment**: Bearish indicator (📉)
- **Confidence scoring**: Each headline gets a confidence score

## 🔧 Technical Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   Streamlit UI  │ ←→ │ Python Logic │ ←→ │ External APIs   │
└─────────────────┘    └──────────────┘    └─────────────────┘
                              │                     │
                              ├── Yahoo Finance ────┤
                              ├── NewsAPI ──────────┤  
                              └── HuggingFace ──────┘
```

## 📸 Output Screenshots for **APPLE** Stock

<img width="720" height="540" alt="image" src="https://github.com/user-attachments/assets/b90d8fa3-fc6c-47fb-9e10-47f9da169afe" />

<img width="720" height="540" alt="image" src="https://github.com/user-attachments/assets/db14dcc5-f805-4d9d-bb21-10ce4524eac6" />

## ⚠️ Important Notes

- **API Limits**: NewsAPI has rate limits on free tier
- **Market Hours**: Stock prices update during market hours
- **News Availability**: Some stocks may have limited news coverage
- **Sentiment Accuracy**: AI sentiment is indicative, not financial advice

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚖️ Disclaimer

This tool is for educational and research purposes only. It does not constitute financial advice. Always do your own research and consult with qualified financial advisors before making investment decisions.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) for stock data
- [NewsAPI](https://newsapi.org/) for news headlines
- [Hugging Face](https://huggingface.co/) for sentiment analysis models
- [Streamlit](https://streamlit.io/) for the web framework

---

**Made with ❤️ and Python**
