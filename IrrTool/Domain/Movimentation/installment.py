from typing import List
import pandas as pd
from IrrTool.Application.interfaces import IMovimentation


class Installment(IMovimentation):
    dataframe: pd.DataFrame
    content: List[dict]

    def __init__(self, content: List[dict]) -> None:
        self.content = content

    def prepare(self):
        self.dataframe = pd.DataFrame(
            self.content,
            columns=['investment_id', 'due_date', 'amount']
        )
        self.dataframe = self.dataframe.dropna()
        self.dataframe['investment_id'] = self.dataframe['investment_id'].astype(int)
        self.dataframe['due_date'] = pd.to_datetime(self.dataframe['due_date'])
        self.dataframe['amount'] = pd.to_numeric(self.dataframe['amount'])
        self.dataframe.rename(
            columns={'investment_id': 'id', 'due_date': 'date'},
            inplace=True
        )
