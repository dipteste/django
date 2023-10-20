import random
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Substitua 'SEU_TOKEN' pelo token do seu bot
TOKEN = '6489141552:AAHwlOc3cN4kR1dNGn4OYfm83uvKZ6wJ6Ls'

# Substitua 'SEU_CHAT_ID' pelo Chat ID do grupo onde o bot é administrador
CHAT_ID = '-1001779029251'

# Crie uma instância do bot
bot = Bot(token=TOKEN)

# URL do Google
google_url = 'https://t.me/playccsbot'

# URL da imagem que você quer enviar
imagem_url = 'https://i.ibb.co/bJgz6Ly/IMG-20230711-113223-015.jpg'

# Mensagens que o bot enviará
mensagens = [
    

    f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>544731**********|MASTERCARD</code>',
    f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>550209**********|MASTERCARD</code>',
    f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ STANDARD</b>'
    '\n<b>🔹Preço: R$ 10</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>511781**********|MASTERCARD</code>',
    f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ CLASSIC</b>'
    '\n<b>🔹Preço: R$ 10</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>498453**********|VISA</code>',
    f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ PLATINUM</b>'
    '\n<b>🔹Preço: R$ 25</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>515590**********|MASTERCARD</code>',
     f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ STANDARD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>498407**********|MASTERCARD</code>',
     f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ STANDARD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>404042**********|MASTERCARD</code>',
     f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ STANDARD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>490149**********|MASTERCARD</code>',
     f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ NUBANK GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>550209**********|MASTERCARD</code>',
     f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ NUBANK GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>550209**********|MASTERCARD</code>',
     f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ NUBANK GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>550209**********|MASTERCARD</code>',
         f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ NUBANK GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>550209**********|MASTERCARD</code>',
         f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ NUBANK GOLD</b>'
    '\n<b>🔹Preço: R$ 15</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>550209**********|MASTERCARD</code>',
         f'<a href="{imagem_url}">&#8204;</a>💳 Cartão adquirido com sucesso! '
    '\n<b>🔹Nivel: R$ NUBANK PLAT</b>'
    '\n<b>🔹Preço: R$ 25</b>'
    '\n\n<b>🥤Chama na aula! obrigado pela preferencia</b>'
    '\n\n\n<b>- Produto:</b>'
    '\n<code>516292**********|MASTERCARD</code>',
    # ... outras mensagens ...
    f'💰 Subiu <b>R$20.0</b> de saldo, hora da aula!',
    # ... outras mensagens ...
        # ... outras mensagens ...
    f'💰 Subiu <b>R$10.0</b> de saldo, hora da aula!',
    # ... outras mensagens ...
        # ... outras mensagens ...
    f'💰 Subiu <b>R$50.0</b> de saldo, hora da aula!',
 
]

# Lista de intervalos de tempo em segundos (5 timers diferentes)
intervalos = [1700, 680, 870, 1100, 400]

# Valores pré-definidos para o saldo
valores_saldo = [10, 15, 20, 35, 20, 30]

# Variável para controlar se o botão "💳 Compre as melhores ccs" deve ser incluído
incluir_botao = True

async def enviar_mensagem():
    global incluir_botao  # Declare a variável como global
    while True:
        try:
            # Escolha uma mensagem aleatória
            mensagem = random.choice(mensagens)

            # Se for a mensagem com o saldo, exclua o botão e defina um valor pré-definido
            if "Subiu <b>R$10.0</b>" in mensagem:
                valor_saldo = random.choice(valores_saldo)
                mensagem = mensagem.replace('<b>R$10.0</b>', f'<b>R${valor_saldo:.1f}</b>')
                incluir_botao = False
            else:
                incluir_botao = True

            # Crie um botão inline se necessário
            if incluir_botao:
                botao_clique_aqui = InlineKeyboardButton("💳 Compre as melhores ccs", url=google_url)
                teclado_inline = InlineKeyboardMarkup([[botao_clique_aqui]])
            else:
                teclado_inline = None

            # Envie a mensagem com o botão inline (se houver) e a formatação HTML
            await bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode='HTML', reply_markup=teclado_inline)

            print("Mensagem enviada com sucesso!")

        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

        # Escolha aleatoriamente um intervalo de tempo da lista
        intervalo_aleatorio = random.choice(intervalos)
        await asyncio.sleep(intervalo_aleatorio)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(enviar_mensagem())
