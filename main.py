from src.Cron_sintaxe import Sintax
from src.Input_client import Input


def main() -> None:
    """Init the project"""

    data_input_client = Input().exec()
    print(data_input_client)
    sintaxe = Sintax(data_input_client).exec()
    print(f'Sua expressão CRON está pronta = " {sintaxe} "')

if __name__ == '__main__':
    main()