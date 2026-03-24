"""Dashboard routes."""

from flask import Blueprint, current_app, render_template

from app.data.binance_provider import BinanceDataProvider


dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")


@dashboard_bp.route("/")
def index():
    provider = BinanceDataProvider(base_url=current_app.config["BINANCE_BASE_URL"])
    signal = "HOLD"
    error = None

    try:
        market = provider.fetch_ohlcv(symbol="BTCUSDT", interval="1h", limit=2)
        latest_price = float(market.iloc[-1]["close"])
    except RuntimeError as exc:
        latest_price = None
        error = str(exc)

    return render_template(
        "dashboard/index.html",
        price=latest_price,
        signal=signal,
        error=error,
        trades=[],
        pnl=0.0,
    )
