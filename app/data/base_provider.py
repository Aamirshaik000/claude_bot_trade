"""Base interfaces for market data providers.

Extend this class for Gold/Oil providers in future.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseDataProvider(ABC):
    """Common interface for all asset data providers."""

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, interval: str = "1h", limit: int = 200) -> pd.DataFrame:
        """Fetch OHLCV data as a pandas DataFrame."""
        raise NotImplementedError
