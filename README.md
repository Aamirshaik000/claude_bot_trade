# claude_bot_trade

Modular Flask-based algorithmic trading bot scaffold.

## Implemented in this iteration
- Task 1: project setup and modular package structure.
- Task 2: BTC OHLCV data engine using Binance public API.
- Base Flask dashboard showing live BTC price, placeholder signal, trade history, and PnL.
- Dashboard auto-refresh for market data every second via `/api/market`.

## Project structure

```
.
├── app.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── data/
    │   ├── __init__.py
    │   ├── base_provider.py
    │   └── binance_provider.py
    ├── indicators/
    ├── strategy/
    ├── risk/
    ├── execution/
    ├── ai/
    └── dashboard/
        ├── __init__.py
        ├── routes.py
        └── templates/
            └── dashboard/
                └── index.html
```

## Run locally

### 1) Clone and enter the repo
```bash
git clone <your-repo-url>
cd claude_bot_trade
```

### 2) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4) Start the Flask app
```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

### Troubleshooting
- If you see `ModuleNotFoundError: No module named flask`, re-run dependency installation in the same active virtual environment.
- If port 5000 is already in use, run: `FLASK_RUN_PORT=5001 python app.py` and then open `http://127.0.0.1:5001`.


### Live updates
- The dashboard page polls `/api/market` every 1 second to refresh price/signal without a full page reload.
