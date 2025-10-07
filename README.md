# AI-Based Microcap Token Pump/Dump Detector

This project uses AI/ML to detect potential pump or dump events for microcap tokens. It analyzes historical token data, trading volume, holder distribution, and social media sentiment to provide early alerts.

## Features

- Detect potential pump/dump events for microcap tokens
- Historical data analysis and feature engineering
- Optional social media sentiment integration (Twitter, Telegram)
- Visualize alerts and trends with a minimal dashboard
- Offline mode with CSV/JSON for testing

## All-in-One Installation, Usage, Backend, Guide, and Notes

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/microcap-pump-dump-detector.git
cd microcap-pump-dump-detector

# 2. Install Python dependencies
pip install pandas scikit-learn xgboost matplotlib plotly requests

# 3. Optional: Install frontend dependencies for dashboard
cd dashboard
npm install

# 4. Backend Usage (Python AI)
python scripts/fetch_data.py        # Fetch token historical and volume data
python scripts/feature_engineering.py  # Prepare features for ML model
python scripts/train_model.py       # Train pump/dump detector
python scripts/predict_alerts.py    # Generate alerts

# 5. Frontend Dashboard (Optional)
cd dashboard
npm run dev
# Open http://localhost:5173 to see visualizations

# 6. Notes
# - Designed for educational/research purposes, not financial advice
# - Token data can be fetched from CoinGecko, DEX API, or CSV offline
# - Social media sentiment requires API keys for Twitter/Telegram
# - Adjust model parameters for different microcap tokens
