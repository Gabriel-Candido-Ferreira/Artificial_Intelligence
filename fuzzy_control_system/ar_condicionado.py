import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
pessoas = ctrl.Antecedent(np.arange(0, 21, 1), 'pessoas')
hora = ctrl.Antecedent(np.arange(0, 24, 1), 'hora')

resfriamento = ctrl.Consequent(np.arange(0, 101, 1), 'resfriamento')

temperatura['frio'] = fuzz.trimf(temperatura.universe, [0, 0, 18])
temperatura['agradavel'] = fuzz.trimf(temperatura.universe, [16, 22, 28])
temperatura['quente'] = fuzz.trimf(temperatura.universe, [26, 40, 40])

pessoas['poucas'] = fuzz.trimf(pessoas.universe, [0, 0, 6])
pessoas['media'] = fuzz.trimf(pessoas.universe, [4, 10, 16])
pessoas['muitas'] = fuzz.trimf(pessoas.universe, [14, 20, 20])

hora['manha'] = fuzz.trimf(hora.universe, [0, 6, 11])
hora['tarde'] = fuzz.trimf(hora.universe, [10, 15, 18])
hora['noite'] = fuzz.trimf(hora.universe, [17, 21, 23])

resfriamento['baixo'] = fuzz.trimf(resfriamento.universe, [0, 0, 40])
resfriamento['medio'] = fuzz.trimf(resfriamento.universe, [30, 50, 70])
resfriamento['alto'] = fuzz.trimf(resfriamento.universe, [60, 100, 100])

regras = [
    ctrl.Rule(temperatura['frio'], resfriamento['baixo']),
    ctrl.Rule(temperatura['agradavel'] & pessoas['poucas'], resfriamento['baixo']),
    ctrl.Rule(temperatura['agradavel'] & pessoas['media'], resfriamento['medio']),
    ctrl.Rule(temperatura['agradavel'] & pessoas['muitas'], resfriamento['alto']),
    ctrl.Rule(temperatura['quente'] & pessoas['poucas'], resfriamento['medio']),
    ctrl.Rule(temperatura['quente'] & pessoas['muitas'], resfriamento['alto']),
    ctrl.Rule(temperatura['quente'] & hora['tarde'], resfriamento['alto']),
    ctrl.Rule(temperatura['agradavel'] & hora['noite'], resfriamento['baixo']),
    ctrl.Rule(temperatura['quente'] & hora['noite'], resfriamento['medio']),
]

ac_ctrl = ctrl.ControlSystem(regras)
ac_simulador = ctrl.ControlSystemSimulation(ac_ctrl)

ac_simulador.input['temperatura'] = 30
ac_simulador.input['pessoas'] = 5
ac_simulador.input['hora'] = 14

ac_simulador.compute()
print(f"Nível de resfriamento recomendado: {ac_simulador.output['resfriamento']:.2f}%")

temperatura.view()
pessoas.view()
hora.view()
resfriamento.view()
resfriamento.view(sim=ac_simulador)
plt.show()