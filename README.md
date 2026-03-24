# claude_bot_trade

Modular Flask-based algorithmic trading bot scaffold.

## Implemented in this iteration
- Task 1: project setup and modular package structure.
- Task 2: BTC OHLCV data engine using Binance public API.
- Base Flask dashboard showing live BTC price, placeholder signal, trade history, and PnL.

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
            └── index.html
```

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.
