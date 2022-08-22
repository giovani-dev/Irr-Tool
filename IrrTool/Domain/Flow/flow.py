from datetime import timedelta
from typing import Any, Dict
import pandas as pd

from IrrTool.Application.interfaces import IMovimentation


class CashFlow:
    investment: IMovimentation
    installment: IMovimentation
    dataframe: pd.DataFrame
    content: Dict[int, Any] = {}

    def __init__(self, investment: IMovimentation, installment: IMovimentation) -> None:
        self.investment = investment
        self.installment = installment

    def _generate_dates(self) -> None:
        for n_frame in range(0, len(self.dataframe.date)):
            if n_frame != len(self.dataframe.date) - 1:
                date_range = pd.date_range(
                    start=self.dataframe.date[n_frame] + timedelta(days=1),
                    end=self.dataframe.date[n_frame + 1] - timedelta(days=1),
                )
                self.dataframe = pd.concat(
                    [
                        self.dataframe,
                        pd.DataFrame(
                            {"date": date_range, "amount": [0] * len(date_range)}
                        ),
                    ],
                    ignore_index=True,
                )

    def execute(self):
        for _id in self.investment.dataframe["id"]:
            self.dataframe = self.installment.dataframe.where(
                self.installment.dataframe["id"] == _id
            ).dropna()
            sliced_investment = self.investment.dataframe.where(
                self.investment.dataframe["id"] == _id
            ).dropna()
            self.dataframe = pd.concat(
                [self.dataframe, sliced_investment], ignore_index=True
            ).sort_values(by=["date"], ignore_index=True)
            self._generate_dates()
            self.content[_id] = self.dataframe
            self.dataframe = (
                self.dataframe.sort_values(by=["date"], ignore_index=True)
                .groupby(["date"])
                .sum()
            )
            self.content[_id] = list(self.dataframe["amount"])
