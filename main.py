import datetime
import flet as ft

total_economizado = 0
historial = []

def calcular_desconto(preco, desconto):
    return preco - preco * desconto / 100, preco * desconto / 100

def verificar_brinde(valor):
    if 100 <= valor < 150:
        return "Leve coração 💖 e Stickers rosas ou azul"
    elif 150 <= valor < 200:
        return "Marca páginas + pulseira code girl/boy + Frete grátis"
    elif valor >= 200:
        return "Mini quaderno (Meus ahorros cute) 🎀"
    else:
        return "Sem brinde ainda. Falta pouco!"

def main(page: ft.Page):
    global total_economizado
    page.title = "Calculadora Rosa"
    page.bgcolor = "#FFF0F5"
    page.scroll = ft.ScrollMode.AUTO

    preco_input = ft.TextField(label="Preço original (R$)", value="100", keyboard_type=ft.KeyboardType.NUMBER)
    desconto_input = ft.TextField(label="Desconto (%)", value="10", keyboard_type=ft.KeyboardType.NUMBER)
    limite_desc_input = ft.TextField(label="Limite máx. de desconto (%)", value="30", keyboard_type=ft.KeyboardType.NUMBER)
    limite_gasto_input = ft.TextField(label="Seu limite máx. de gasto (R$)", value="200", keyboard_type=ft.KeyboardType.NUMBER)

    alertas_text = ft.Text("", size=16, weight=ft.FontWeight.BOLD)
    comprovante_text = ft.Text("", size=14)
    historial_text = ft.Text("", size=14)

    def processar(e):
        global total_economizado
        try:
            preco = float(preco_input.value)
            desconto = float(desconto_input.value)
            limite_desconto = float(limite_desc_input.value)
            limite_gasto = float(limite_gasto_input.value)
        except:
            alertas_text.value = "❌ Preencha todos com números!"
            page.update()
            return

        if preco <= 0:
            alertas_text.value = "❌ O preço tem que ser maior que 0!"
            page.update()
            return

        valor_final, economia = calcular_desconto(preco, desconto)
        brinde = verificar_brinde(valor_final)

        alertas = []
        if desconto > limite_desconto:
            alertas.append("🎀 ALERTA ROSA: Passou do seu limite!")
        if valor_final > limite_gasto:
            alertas.append("⚠️ ALERTA: Passou do seu orçamento!")
        alertas_text.value = "\n".join(alertas) if alertas else "✅ Tudo dentro dos seus limites!"

        total_economizado += economia
        historial.append(f"R${valor_final:.2f} - Brinde: {brinde}")
        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        comprovante_text.value = f"--- COMPROVANTE ROSA ---\nData: {agora}\nPreço: R${preco:.2f}\nDesconto: {desconto}%\nVocê economizou: R${economia:.2f}\nValor final: R${valor_final:.2f}\nBrinde: {brinde}"
        historial_text.value = f"💰 Total economizado: R${total_economizado:.2f}\n\n" + "\n".join(historial)
        page.update()

    btn = ft.ElevatedButton("🎀 Calcular", on_click=processar, bgcolor="#FF69B4", color="white", width=200, height=50)
    page.add(
        ft.Text("🎀 Minha Calculadora Rosa 🎀", size=24, weight=ft.FontWeight.BOLD, color="#FF1493", text_align=ft.TextAlign.CENTER),
        preco_input, desconto_input, limite_desc_input, limite_gasto_input, btn,
        ft.Divider(), ft.Text("Status e Alertas", weight=ft.FontWeight.BOLD), alertas_text,
        ft.Text("Comprovante Rosa", weight=ft.FontWeight.BOLD), comprovante_text,
        ft.Text("Historial do Dia", weight=ft.FontWeight.BOLD), historial_text,
    )

ft.app(target=main)
