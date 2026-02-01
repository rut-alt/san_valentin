import streamlit as st
import random

st.set_page_config(page_title="💘 San Valentín 💘", layout="centered")

# ---------- ESTADOS ----------
if "step" not in st.session_state:
    st.session_state.step = 1

if "no_position" not in st.session_state:
    st.session_state.no_position = random.randint(0, 2)

# ---------- STEP 1 ----------
if st.session_state.step == 1:
    st.markdown(
        "<h1 style='text-align:center; color:#e60073;'>"
        "¿Quieres una cita conmigo el 14 de febrero? 💖"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💘 SÍ 💘"):
        st.session_state.step = 2
        st.rerun()

    cols = st.columns(3)
    if cols[st.session_state.no_position].button("NO 🙄"):
        st.session_state.no_position = random.randint(0, 2)
        st.rerun()

# ---------- STEP 2 ----------
elif st.session_state.step == 2:
    st.markdown(
        "<h1 style='text-align:center;'>¿Qué te gustaría cenar? 😋</h1>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.image("images/sushi.jpg", use_container_width=True)
        if st.button("🍣 Sushi"):
            st.success("Perfecto 😍 Sushi it is!")

    with col2:
        st.image("images/carne.jpg", use_container_width=True)
        if st.button("🥩 Carne"):
            st.success("Ufff, planazo 🥩🔥")

    with col3:
        st.image("images/ami.jpg", use_container_width=True)
        if st.button("😏 A mí"):
            st.warning("ANDA TONTO 😂 ese es el postre!! ¡Elige bien!")

    with col4:
        st.markdown("### 🤷‍♂️ Otro")
        otro = st.text_input("¿Qué te apetece?", placeholder="Escribe aquí...")

        if otro:
            st.success(f"Perfecto 😌 entonces será: **{otro}**")

    st.markdown("<br>")
    st.balloons()

