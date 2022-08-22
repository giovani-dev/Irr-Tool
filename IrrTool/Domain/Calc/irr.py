from typing import Dict, List
from IrrTool.Domain.Flow.flow import CashFlow
import numpy_financial as npf
import concurrent.futures


class CalcIrr:
    def __init__(self, flow: CashFlow) -> None:
        self._flow = flow

    def from_one(self, _id: int) -> Dict[int, float]:
        return {_id: npf.irr(self._flow.content[_id])}

    def from_all(self) -> Dict[int, float]:
        result = {}
        for key in self._flow.content.keys():
            result[key] = npf.irr(self._flow.content[key])
        return result

    def from_id_list(self, id_list: List[int]) -> Dict[int, float]:
        result = {_id: npf.irr(self._flow.content[_id]) for _id in id_list}
        return result
