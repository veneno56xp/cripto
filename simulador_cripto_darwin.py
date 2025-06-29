
import streamlit as st

st.set_page_config(page_title="Simulador Cripto", page_icon="📈")

st.title("📊 Simulador de Inversión en Criptomonedas")
st.markdown("Simula cuánto ganarías invirtiendo en distintas criptomonedas con escenarios realistas (optimista, neutro, pesimista).")

monedas = {
    "Bitcoin (BTC)": 65000,
    "Ethereum (ETH)": 3500,
    "Solana (SOL)": 145,
    "Ripple (XRP)": 0.55,
    "Pepe (PEPE)": 0.000011
}

moneda = st.selectbox("Selecciona la criptomoneda:", list(monedas.keys()))
precio_actual = monedas[moneda]

inversion = st.slider("¿Cuánto deseas invertir? (USD)", 10, 1000, 100, step=10)

precio_optimista = precio_actual * 1.3
precio_neutro = precio_actual
precio_pesimista = precio_actual * 0.8

cantidad_comprada = inversion / precio_actual
valor_optimista = cantidad_comprada * precio_optimista
valor_neutro = cantidad_comprada * precio_neutro
valor_pesimista = cantidad_comprada * precio_pesimista

st.markdown(f"### Resultados para {moneda}")
st.write(f"🔸 Precio actual: ${precio_actual}")
st.write(f"🔸 Cripto que comprarías: {cantidad_comprada:.6f}")
st.write("---")
st.success(f"📈 Optimista: ${valor_optimista:.2f} (Ganancia: ${valor_optimista - inversion:.2f})")
st.info(f"➖ Neutro: ${valor_neutro:.2f} (±$0)")
st.error(f"📉 Pesimista: ${valor_pesimista:.2f} (Pérdida: ${valor_pesimista - inversion:.2f})")

st.caption("Hecho por ChatGPT para Darwin 🚀")
