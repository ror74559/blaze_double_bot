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
    "password": "sua senha na BlazeL",
    "bet_amount": valor das apostas,
    "stop_loss_ratio": porcentagem da banca inicial para parada quando houver perdas,
    "stop_win_ratio": porcentagem da banca inicial para parada quando houver ganhos,
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

Essa estratégia é apenas um exemplo, podendo ser configurada nesse mesmo padrão, as listas podem
conter até 20 elementos, Use apenas "R" para vermelho "B" para preto.
As listas que ficaren dentro de "red" serão para apostar no vermelho e as que ficarem em "black" para apostar no preto.

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
