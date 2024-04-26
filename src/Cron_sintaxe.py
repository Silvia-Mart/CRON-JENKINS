
class Sintax:

    def __init__(self, list_data_input) -> None:
        self.min = list_data_input[0]
        self.hour = list_data_input[1] 
        self.day_month = list_data_input[2] 
        self.month = list_data_input[3] 
        self.day_week = list_data_input[4] 
        

    def exec(self) -> str:
        return self.sintaxe()

    def sintaxe(self) -> str:

        hour = self.hour.split(',')
        day_m = self.day_month.split(',')
        month = self.month.split(',')
        day_w = self.day_week.split(',')

        self.cron = ''
        week = []
        erro = False

        # min = '*' (0-59)
        list_min = ['*','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59'] 
        min = self.min
        if min not in list_min: 
            print('Valor do minuto fora dos padrões.')
            erro = True
        
        if erro == False:

            # hour = '*' (0-23) 
            list_hour = ['*','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
            for item in hour: 
                if item not in list_hour: 
                    print('Valor da hora fora dos padrões.')
                    erro = True
                 
        if erro == False:

            # day_month = '*' (1-31) 
            list_day_m = ['*','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
            for item in day_m:
                if item not in list_day_m: 
                    print('Valor do dia do mês fora dos padrões.')
                    erro = True

        if erro == False:

            # month = '*' (1-12) 
            list_month = ['*','0','1','2','3','4','5','6','7','8','9','10','11','12']
            for item in month:
                if item not in list_month: 
                    print('Valor do mês fora dos padrões.')
                    erro = True

        if erro == False:

            # day_week = '*' (0-6)
            
            list_week =['*','domingo','segunda','terca','quarta','quinta','sexta','sábado'] 
            for item in day_w:
                if item == 'domingo':
                    week.append('0')
                if item == 'segunda' :
                    week.append('1')
                if item == 'terca':
                    week.append('2')
                if item == 'quarta':
                    week.append('3')
                if item == 'quinta':
                    week.append('4')
                if item == 'sexta':
                    week.append('5')
                if item == 'sábado':
                    week.append('6')

                if item not in list_week: 
                    print('Valor do dia da semana fora dos padrões.')
                    erro = True
                
        
        if erro == False:
            h = self.hour.replace(',','-')
            d_m = self.day_month.replace(',','-')
            m = self.month.replace(',','-')

            string_final = ",".join(week)
            d_w = string_final.replace(',','-')

            self.cron = f'{min} {h} {d_m} {m} {d_w}'

        return self.cron
