import streamlit as st
import random

st.set_page_config(
    page_title="💘 San Valentín 💘",
    layout="centered"
)

st.markdown(
    """
    <h1 style="text-align:center; color:#e60073;">
    ¿Quieres una cita conmigo el 14 de febrero? 💖
    </h1>
    """,
    unsafe_allow_html=True
)

# Estado para controlar el NO
if "no_position" not in st.session_state:
    st.session_state.no_position = random.randint(0, 2)

# Botón SÍ (grande y evidente)
st.markdown("<br>", unsafe_allow_html=True)
if st.button("💘 SÍ 💘"):
    st.success("🥰 Sabía que dirías que sí 🥰")
    st.balloons()
    st.markdown(
        "<h2 style='text-align:center;'>Prepárate para una cita inolvidable 💕</h2>",
        unsafe_allow_html=True
    )
    st.stop()

st.markdown("<br><br>", unsafe_allow_html=True)

# Botón NO que se mueve
cols = st.columns(3)

if cols[st.session_state.no_position].button("NO 🙄"):
    st.session_state.no_position = rando
