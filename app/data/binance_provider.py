"""Binance data provider for BTC OHLCV data."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd
import requests

from .base_provider import BaseDataProvider


@dataclass
class BinanceDataProvider(BaseDataProvider):
    """Fetch market candles from Binance public REST API."""

    base_url: str = "https://api.binance.com"
    timeout: int = 10

    def fetch_ohlcv(self, symbol: str = "BTCUSDT", interval: str = "1h", limit: int = 200) -> pd.DataFrame:
        endpoint = f"{self.base_url}/api/v3/klines"
        params = {"symbol": symbol.upper(), "interval": interval, "limit": limit}

        try:
            response = requests.get(endpoint, params=params, timeout=self.timeout)
            response.raise_for_status()
            rows: list[list[Any]] = response.json()
        except requests.RequestException as exc:
            raise RuntimeError(f"Failed to fetch Binance OHLCV data: {exc}") from exc

        if not rows:
            raise RuntimeError("Binance returned empty OHLCV response")

        frame = pd.DataFrame(
            rows,
            columns=[
                "open_time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_asset_volume",
                "number_of_trades",
                "taker_buy_base_volume",
                "taker_buy_quote_volume",
                "ignore",
            ],
        )

        numeric_columns = ["open", "high", "low", "close", "volume"]
        for col in numeric_columns:
            frame[col] = pd.to_numeric(frame[col], errors="coerce")

        frame["open_time"] = pd.to_datetime(frame["open_time"], unit="ms", utc=True)
        frame["close_time"] = pd.to_datetime(frame["close_time"], unit="ms", utc=True)
        frame = frame.dropna(subset=numeric_columns)

        return frame[["open_time", "open", "high", "low", "close", "volume", "close_time"]]
