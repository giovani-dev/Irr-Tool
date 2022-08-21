import argparse
from IrrTool.Domain.Calc.irr import CalcIrr
from IrrTool.Domain.Flow.flow import CashFlow
from IrrTool.Domain.Movimentation.installment import Installment
from IrrTool.Domain.Movimentation.investment import Investment

from IrrTool.Infraestructure.load_from_json import LoadFromjson


loader = LoadFromjson()

installment = Installment(
    content=loader.load(path='./static/installments.json')['installments']
)
investment = Investment(
    content=loader.load(path='./static/investments.json')['investments']
)
investment.prepare()
installment.prepare()

flow = CashFlow(
    investment=investment,
    installment=installment
)
flow.execute()

calc = CalcIrr(flow)
calc.from_all()
calc.from_one(_id=36)