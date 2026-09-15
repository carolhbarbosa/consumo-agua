# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Energia](https://img.shields.io/badge/tema-consci%C3%AAncia%20h%C3%ADdrica-00B4D8?style=for-the-badge&logo=leaflet&logoColor=white)

## 🎯 Objetivo

Script em Python desenvolvido para uma campanha de conscientização ambiental
da companhia de saneamento local. O programa classifica o perfil de consumo
de água de um imóvel e emite um alerta educativo ao morador, com base no tipo
do imóvel (comercial, casa ou apartamento) e no consumo mensal informado.

## 🐍 Linguagem

Python 3.10 ou superior.

## ▶️ Como executar

```bash
python3 app.py
```

O programa vai pedir:
1. O tipo do imóvel (`comercial`, `casa` ou `apartamento`)
2. O consumo mensal de água em m³ (pode ser decimal, ex.: `12.5`)

E vai responder com a classificação do consumo.

## 📐 Regras de negócio

| Situação | Classificação |
|---|---|
| Imóvel comercial | Tarifa comercial aplicada |
| Apartamento com consumo menor que 10 m³ | Consumo econômico |
| Apartamento ou casa com consumo até 25 m³ | Consumo moderado |
| Qualquer outro caso (acima do limite residencial) | Consumo excessivo |

## 🛠️ Tecnologias

- Python (operadores lógicos `and`/`or` e estrutura condicional `if/elif/else`)