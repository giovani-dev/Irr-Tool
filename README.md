## Instalação
- Crie um ambiente virtual
    - ```python -m virtualenv .venv```
- Ative o ambiente virtual
- Dentro do repositorio irr-tool
    - ``` pip install -e . ```

## Execução
- Calcular o TIR de todos os investimentos
    - ```python IrrTool/Presentation/irr.py```
    - ```python IrrTool/Presentation/irr.py --all <qualquer-valor>```
- Calcular o TIR de um unico investimento
    - ```python IrrTool/Presentation/irr.py --id <id-investimento>```
- Calcular o TIR de 2 ou mais investimentos
    - ```python IrrTool/Presentation/irr.py  --id <id-investimento> <id-investimento>```