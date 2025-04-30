
```markdown
# ❄️ Sistema Fuzzy de Controle de Ar-Condicionado

Este projeto é uma simulação de um sistema fuzzy desenvolvido em Python com a biblioteca `scikit-fuzzy`. Ele tem como objetivo controlar o nível de resfriamento de um ar-condicionado com base em três variáveis de entrada:

- 🌡️ Temperatura ambiente
- 👥 Quantidade de pessoas no ambiente
- 🕒 Hora do dia

---

## 📌 Objetivo

Simular um sistema de controle inteligente para ar-condicionado que seja capaz de tomar decisões aproximadas, semelhantes às humanas, mesmo diante de incertezas e imprecisões nas entradas.

---

## ⚙️ Como funciona

### Entradas fuzzy

| Variável     | Termos Linguísticos | Intervalo       |
|--------------|---------------------|------------------|
| Temperatura  | Frio, Agradável, Quente | 0 a 40 ºC      |
| Pessoas      | Poucas, Média, Muitas   | 0 a 20          |
| Hora         | Manhã, Tarde, Noite     | 0 a 23 (horas)  |

### Saída fuzzy

| Variável       | Termos Linguísticos | Intervalo        |
|----------------|---------------------|------------------|
| Resfriamento   | Baixo, Médio, Alto  | 0 a 100 (%)      |

---

## 📖 Regras Fuzzy

O sistema utiliza regras do tipo **SE...ENTÃO**, como por exemplo:

- SE temperatura é quente E pessoas são muitas → ENTÃO resfriamento é alto  
- SE temperatura é agradável E pessoas são poucas → ENTÃO resfriamento é médio  
- SE temperatura é fria → ENTÃO resfriamento é baixo  
- SE hora é tarde E temperatura é quente → ENTÃO resfriamento é alto  
- ...

Essas regras imitam o raciocínio humano de forma interpretável e flexível.

---

## 🖼️ Visualização

O sistema plota os gráficos de:
- Funções de pertinência das entradas e da saída
- Resultado final da inferência fuzzy

Para visualizar os gráficos, adicione ao final do script:

```python
resfriamento.view(sim=ac_simulador)
plt.show()
```

---

## ▶️ Como executar

### Pré-requisitos

- Python 3.x
- scikit-fuzzy
- matplotlib
- numpy

### Instalação dos pacotes:

```bash
pip install scikit-fuzzy matplotlib numpy
```

### Rodando o script

```bash
python fuzzy_arcondicionado.py
```

---

## 📈 Exemplo de uso

```python
ac_simulador.input['temperatura'] = 30
ac_simulador.input['pessoas'] = 5
ac_simulador.input['hora'] = 14
ac_simulador.compute()
print(f"Nível de resfriamento: {ac_simulador.output['resfriamento']:.2f}%")
```

Saída esperada:

```
Nível de resfriamento: 73.45%
```

---

## 📚 Tecnologias usadas

- Python
- [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy)
- matplotlib
- numpy

---

## 🧠 Conceitos aplicados

- Lógica fuzzy
- Funções de pertinência (triangular)
- Inferência Mamdani
- Defuzzificação (centroide)

---
