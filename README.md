# Blaze Double Bot

---

## Description

This Python script automates the betting process on the Blaze Double website using Selenium and undetected-chromedriver. It monitors the game state, places bets according to a predefined strategy, and handles winnings and losses.

---

## Installation

To install and use the bot, follow these steps:

git clone https://github.com/seu-usuario/blaze-double-bot.git

cd blaze-double-bot

pip install -r requirements.txt


---

## How to use the JSON file in the Blaze Double Bot

To use the Blaze Double Bot, you need to configure your credentials and other settings through a JSON file. Follow the instructions below to set up and use the bot:

1. **Create a `config.json` file** with the following content:

```json
{
    "username": "your blaze username",
    "password": "your blaze password",
    "bet_amount":,
    "stop_loss_ratio": ,
    "stop_win_ratio":,
    "strategies": {
        "red": [
            ["B", "R", "B", "R", "B"],
            ["B", "B", "B", "B", "B"]
        ],
        "black": [
            ["R", "B", "R", "B", "R"],
            ["R", "R", "R", "R", "R"]
        ]
    }
}

```

- **username**: Your username or email registered on Blaze Double.
- **password**: Your password to access Blaze Double.
- **bet_amount**: The amount of the bet to be placed in each round.
- **stop_loss_ratio**: The multiplication factor of the initial balance indicating the loss limit. The bot will stop betting if the balance drops below this limit.
- **stop_win_ratio**: The multiplication factor of the initial balance indicating the win limit. The bot will stop betting if the balance reaches or exceeds this limit.
- **strategies**: Pre-defined betting strategies with sequences of colors (black = "B", red = "R"). You can add as many strategies as you want here.

## Usage

To run the bot:

python bot.py


---

## Support This Project

If you find this project helpful, consider supporting it by making a donation. Your contribution will help me maintain and improve this bot.

[Donate via PayPal](https://www.paypal.com/donate?hosted_button_id=SEU-CÓDIGO-DO-BOTÃO)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Blaze Double Bot -> Português

---

## Descrição

Este script em Python automatiza o processo de apostas no site Blaze Double usando Selenium e undetected-chromedriver. Ele monitora o estado do jogo, realiza apostas de acordo com uma estratégia predefinida e gerencia ganhos e perdas.

---

## Instalação

Para instalar e usar o bot, siga estes passos:

git clone https://github.com/seu-usuario/blaze-double-bot.git

cd blaze-double-bot

pip install -r requirements.txt


---

## Como usar o arquivo JSON no Blaze Double Bot

Para usar o Blaze Double Bot, você precisará configurar suas credenciais e outras configurações através de um arquivo JSON. Siga as instruções abaixo para configurar e utilizar o bot:

1. **Crie um arquivo `config.json`** com o seguinte conteúdo:

```json
{
    "username": "seu usuario da blaze",
    "password": "sua senha na Blaze",
    "bet_amount": ,
    "stop_loss_ratio": ,
    "stop_win_ratio": ,
    "strategies": {
        "red": [
            ["B", "R", "B", "R", "B"],
            ["B", "B", "B", "B", "B"]
        ],
        "black": [
            ["R", "B", "R", "B", "R"],
            ["R", "R", "R", "R", "R"]
        ]
    }
}
```
- **username**: Seu nome de usuário ou e-mail cadastrado no Blaze Double.
- **password**: Sua senha para acessar o Blaze Double.
- **bet_amount**: O valor da aposta que será realizada em cada rodada.
- **stop_loss_ratio**: O fator de multiplicação do saldo inicial que indica o limite de perda. O bot irá parar de apostar se o saldo cair abaixo desse limite.
- **stop_win_ratio**: O fator de multiplicação do saldo inicial que indica o limite de ganho. O bot irá parar de apostar se o saldo atingir ou ultrapassar esse limite.
- **strategies**: Estratégias de aposta pré-definidas com sequências de cores (preto = "B", vermelho = "R"). Você pode adicionar quantas estratégias quiser aqui.

---
## Uso


Para executar o bot:

python bot.py


---

## Apoie Este Projeto

Se você achar este projeto útil, considere apoiá-lo fazendo uma doação. Sua contribuição ajudará a manter e melhorar este bot.

[Doar via PayPal](https://www.paypal.com/donate?hosted_button_id=SEU-CÓDIGO-DO-BOTÃO)

---

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

© 2024 Rafael Ribeiro.
