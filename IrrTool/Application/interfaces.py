from abc import ABC, abstractmethod
from typing import Any, Dict, List
import pandas as pd


class IMovimentation(ABC):
    dataframe: pd.DataFrame
    content: List[dict]

    @abstractmethod
    def prepare(self):
        ...


class IFlow(ABC):
    investment: IMovimentation
    installment: IMovimentation
    dataframe: pd.DataFrame
    flow: Dict[int, Any]

    @abstractmethod
    def execute(self) -> None:
        ...
