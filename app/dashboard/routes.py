"""Dashboard routes."""

from flask import Blueprint, current_app, jsonify, render_template

from app.data.binance_provider import BinanceDataProvider


dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")


def _get_market_snapshot() -> dict:
    """Fetch the latest BTC market snapshot for dashboard use."""
    provider = BinanceDataProvider(base_url=current_app.config["BINANCE_BASE_URL"])

    signal = "HOLD"
    error = None
    latest_price = None

    try:
        market = provider.fetch_ohlcv(symbol="BTCUSDT", interval="1h", limit=2)
        latest_price = float(market.iloc[-1]["close"])
    except RuntimeError as exc:
        error = str(exc)

    return {
        "price": latest_price,
        "signal": signal,
        "error": error,
    }


@dashboard_bp.route("/")
def index():
    snapshot = _get_market_snapshot()
    return render_template(
        "dashboard/index.html",
        price=snapshot["price"],
        signal=snapshot["signal"],
        error=snapshot["error"],
        trades=[],
        pnl=0.0,
    )


@dashboard_bp.route("/api/market")
def market_data():
    """Return latest market data for client-side dashboard polling."""
    snapshot = _get_market_snapshot()
    return jsonify(snapshot)
