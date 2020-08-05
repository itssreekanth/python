import pandas as pd
def answer_one():
    energy = pd.read_excel('Energy Indicators.xls')
    energy.columns = [energy.columns[0],energy.columns[1],'Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy = energy['Energy Supply']
    return energy
a = answer_one()
print(a)