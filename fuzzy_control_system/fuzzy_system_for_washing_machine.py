import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Entradas
sujeira = ctrl.Antecedent(np.arange(0, 11, 1), 'sujeira')
carga = ctrl.Antecedent(np.arange(0, 11, 1), 'carga')

# Saída
tempo = ctrl.Consequent(np.arange(0, 61, 1), 'tempo')

# Funções de pertinência para sujeira
sujeira['baixa'] = fuzz.trimf(sujeira.universe, [0, 0, 5])
sujeira['media'] = fuzz.trimf(sujeira.universe, [2, 5, 8])
sujeira['alta'] = fuzz.trimf(sujeira.universe, [5, 10, 10])

# Funções de pertinência para carga
carga['leve'] = fuzz.trimf(carga.universe, [0, 0, 5])
carga['media'] = fuzz.trimf(carga.universe, [2, 5, 8])
carga['pesada'] = fuzz.trimf(carga.universe, [5, 10, 10])

# Funções de pertinência para tempo
tempo['curto'] = fuzz.trimf(tempo.universe, [0, 0, 20])
tempo['medio'] = fuzz.trimf(tempo.universe, [10, 30, 50])
tempo['longo'] = fuzz.trimf(tempo.universe, [40, 60, 60])

# Regras fuzzy
regra1 = ctrl.Rule(sujeira['baixa'] & carga['leve'], tempo['curto'])
regra2 = ctrl.Rule(sujeira['media'] | carga['media'], tempo['medio'])
regra3 = ctrl.Rule(sujeira['alta'] | carga['pesada'], tempo['longo'])

# Criação do sistema de controle
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema_controle)

# Teste com valores de entrada
simulador.input['sujeira'] = 7  # alto
simulador.input['carga'] = 3    # leve

# Rodar o sistema
simulador.compute()

# Resultado
print(f"Tempo de lavagem recomendado: {simulador.output['tempo']:.2f} minutos")

# Mostrar gráficos das funções de pertinência
sujeira.view()
carga.view()
tempo.view()
tempo.view(sim=simulador)

print("Fim")
