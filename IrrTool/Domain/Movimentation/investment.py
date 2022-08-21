from typing import List
import pandas as pd

from IrrTool.Application.interfaces import IMovimentation


class Investment(IMovimentation):
    dataframe: pd.DataFrame
    content: List[dict]

    def __init__(self, content: List[dict]) -> None:
        self.content = content

    def prepare(self):
        self.dataframe = pd.DataFrame(
            self.content,
            columns=['id', 'created_at', 'amount']
        )
        self.dataframe = self.dataframe.dropna()
        self.dataframe['id'] = self.dataframe['id'].astype(int)
        self.dataframe['created_at'] = pd.to_datetime(self.dataframe['created_at'])
        self.dataframe['amount'] = pd.to_numeric(self.dataframe['amount'])
        self.dataframe['amount'] = self.dataframe['amount'] * -1
        self.dataframe.rename(
            columns={'created_at':'date'},
            inplace=True
        )
