# Sistema Fuzzy para Máquina de Lavar

## 💡 O que é um sistema fuzzy?
Um sistema fuzzy (ou sistema de lógica nebulosa) é um modelo baseado em lógica fuzzy, que simula a forma como humanos tomam decisões imprecisas ou vagas. Ao invés de tomar decisões exatas, como na lógica clássica (0 ou 1), a lógica fuzzy permite valores intermediários (ex: 0.3, 0.8, etc.).

**Exemplo:**  
Em vez de dizer "lavar por 37 minutos", pensamos "lava por um tempo médio".

## 🧺 Objetivo do nosso sistema fuzzy
O objetivo deste sistema é controlar o tempo de lavagem de uma máquina de lavar roupa, com base em duas variáveis de entrada:
- **Sujeira da roupa** (sujeira)
- **Quantidade de roupa** (carga)

A saída do sistema será o **tempo de lavagem** (tempo).

## ⚙️ Como o sistema funciona (Passo a Passo)

### ✅ Passo 1: Definir as variáveis fuzzy
**Entradas:**
- **Sujeira**  
  - Universo: 0 a 10  
  - Conjuntos Linguísticos: baixa, média, alta

- **Carga**  
  - Universo: 0 a 10  
  - Conjuntos Linguísticos: pequena, média, grande

**Saída:**
- **Tempo**  
  - Universo: 0 a 60 minutos  
  - Conjuntos Linguísticos: curto, médio, longo

### ✅ Passo 2: Criar as funções de pertinência
Essas funções indicam o grau de pertencimento de uma entrada a um conjunto linguístico. 

**Exemplo:**  
Se **sujeira = 7**, o valor pode ser:
- 0.2 "média"
- 0.8 "alta"

Essas funções geralmente têm formas triangulares ou trapezoidais.

### ✅ Passo 3: Regras fuzzy (sistema especialista)
O sistema é programado com regras que simulam um especialista.

**Exemplo de regras:**
- **Se** sujeira é baixa **e** carga é pequena → tempo é curto
- **Se** sujeira é alta **e** carga é grande → tempo é longo
- **Se** sujeira é média **e** carga é média → tempo é médio

Essas regras são escritas em linguagem natural e depois convertidas para o sistema fuzzy.

### ✅ Passo 4: Inferência fuzzy
O sistema aplica as regras com base nos valores de entrada e calcula o grau de ativação de cada regra.

**Exemplo:**
- **Sujeira = 7** (alta)
- **Carga = 5** (média)  
Isso ativa as regras relacionadas a "sujeira alta" e "carga média".

### ✅ Passo 5: Defuzzificação
A defuzzificação transforma o resultado nebuloso (fuzzy) em um valor real (crisp). O método mais comum para isso é o **centro de massa**, que calcula a média ponderada das áreas ativadas.

**Resultado:** Um valor real, como 38.5 minutos, será obtido.

## 📊 Sobre o gráfico `tempo.view(sim=simulador)`
Este gráfico mostra:
- As funções de pertinência da saída **tempo**
- Quais conjuntos linguísticos foram ativados
- O valor final do tempo (indicada por uma linha preta vertical)

## 👨‍🏫 Por que usar lógica fuzzy?
- **Simula a forma humana de tomar decisões**, especialmente quando os dados são imprecisos.
- Ideal para situações em que não há fórmulas exatas disponíveis.
- Muito útil para problemas heurísticos e de controle.
- Comum em **eletrodomésticos**, **carros**, **clima**, e outros sistemas.

## 📌 Conclusão
O sistema fuzzy é uma ferramenta poderosa para tomar decisões imprecisas.  
Embora este exemplo seja para controlar o tempo de lavagem em uma máquina de lavar, a mesma lógica pode ser aplicada a outros sistemas, como **caldeiras**, **reatores**, **sistemas hidráulicos**, entre outros.

Utilizando o Python com **scikit-fuzzy**, é possível simular e visualizar sistemas fuzzy de maneira simples e eficaz.