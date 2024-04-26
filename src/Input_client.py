class Input:

    def __init__(self) -> None:
        pass
        
    def exec(self) -> list:
        return self.questions()

    def questions(self) -> list:
        self.data_input = []

        print('Vamos começar a criar sua expressão CRON!!!')
        print('Peço que siga as orientações para uma expressão mais acertiva, Vamos lá!!!')


        hour = input('Digite a hora desejada entre os valores de (0-23) sendo "0" para a meia noite, se for mais de um valor coloque como separador a "," como exemplo: 0,23 se desejar todos informe "*"\n')
        minutes = input('Digite o minuto que deseja entre os valores de (0-59) se desejar todos informe "*" \n')
        day = input('Digite o dia do mês que deseja entre os valores de (1-31) se for mais de um valor coloque como separador a "," como exemplo: 1,31 se desejar todos informe "*"\n')
        month = input('Digite o mês do ano que deseja entre os valores de (1-12) se for mais de um valor coloque como separador a "," como exemplo: 1,12 se desejar todos informe "*"\n')
        day_week = input('Digite o dia da semana que deseja " domingo - segunda - terça - quarta - quinta - sexta - sábado ", se for mais de um valor coloque como separador a "," como exemplo: segunda,terça,quarta se desejar todos informe "*"\n')


        self.data_input.append(minutes)
        self.data_input.append(hour)
        self.data_input.append(day)
        self.data_input.append(month)
        self.data_input.append(day_week)

        return self.data_input