# Classe para calculo de amortizacao com SAC

class SAC:
    def __init__(self, taxa, parcelas, principal):
        self.__taxa = taxa
        self.__parcelas = parcelas
        self.__principal = principal

    def show(self):
        dash = '-' * 42
        amort = self.__principal / self.__parcelas
        saldo = self.__principal
        print(dash)
        print('{:<2}{:>10}{:>10}{:>10}{:>10}'.format('#', 'juros', 'amort', 'pgto', 'saldo'))
        print(dash)
        for n in range(1, self.__parcelas + 1):
            juros = (saldo * self.__taxa) / 100
            pgto = juros + amort
            saldo -= amort
            print('{:<2}{:>10}{:>10}{:>10}{:>10}'.format(n, juros, amort, pgto, saldo))
        print(dash)


"""
Um advogado comprou uma sala para instalar seu escritório por $ 120.000,00 
utilizando o sistema de amortização constante (SAC). O banco financiou a 
compra dessa sala em 24 meses com juros de 2% ao mês. 
"""

sac = SAC(2, 24, 120000)
sac.show()
