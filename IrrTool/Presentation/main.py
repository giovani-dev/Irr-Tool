import argparse
from IrrTool.Domain.Calc.irr import CalcIrr
from IrrTool.Domain.Flow.flow import CashFlow
from IrrTool.Domain.Movimentation.installment import Installment
from IrrTool.Domain.Movimentation.investment import Investment

from IrrTool.Infraestructure.load_from_json import LoadFromjson

parser = argparse.ArgumentParser(
    description="Calculate irr value from investment and installment document"
)
parser.add_argument(
    "--installment",
    help="load installment document",
    default="./static/installments.json",
)
parser.add_argument(
    "--investment", help="load investment document", default="./static/investments.json"
)
parser.add_argument(
    "--id", help="specify the id for the calc", nargs="+", default=[], type=int
)
parser.add_argument("--all", help="irr calc from all investments", action="all")

args = parser.parse_args()

loader = LoadFromjson()

installment = Installment(content=loader.load(path=args.installment)["installments"])
investment = Investment(content=loader.load(path=args.investment)["investments"])
investment.prepare()
installment.prepare()

flow = CashFlow(investment=investment, installment=installment)
flow.execute()

calc = CalcIrr(flow)

result = None

if args.id and len(args.id) > 1:
    print(f"Calculanting irr from {args.id}")
    result = calc.from_id_list(id_list=args.id)
elif args.id and len(args.id) == 1:
    print(f"Calculanting irr from {args.id[0]}")
    result = calc.from_one(_id=args.id[0])
else:
    raise SystemError

if args.all:
    print("Calculating irr from all investments...")
    result = calc.from_all()


def print_irr(content: dict):
    for key in content.keys():
        print(f"Investment [{key}] - {content[key]}")


print_irr(result)
