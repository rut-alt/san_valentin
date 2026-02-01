import streamlit as st
import random

st.set_page_config(page_title="💘 San Valentín 💘", layout="centered")

# ---------- ESTADOS ----------
if "step" not in st.session_state:
    st.session_state.step = 1

if "no_position" not in st.session_state:
    st.session_state.no_position = random.randint(0, 2)

if "cena" not in st.session_state:
    st.session_state.cena = None

if "cena_img" not in st.session_state:
    st.session_state.cena_img = None

if "ropa" not in st.session_state:
    st.session_state.ropa = None

if "ropa_img" not in st.session_state:
    st.session_state.ropa_img = None


# ---------- STEP 1: CITA ----------
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
    if cols[st.session_state.no_position].button("NO "):
        st.session_state.no_position = random.randint(0, 2)
        st.rerun()


# ---------- STEP 2: CENA ----------
elif st.session_state.step == 2:
    st.markdown("<h1 style='text-align:center;'>¿Qué te gustaría cenar? </h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.image("images/sushi.jpg", use_container_width=True)
        if st.button("Sushi"):
            st.session_state.cena = "Sushi"
            st.session_state.cena_img = "images/sushi.jpg"
            st.session_state.step = 3
            st.rerun()

    with col2:
        st.image("images/carne.jpg", use_container_width=True)
        if st.button("Carne"):
            st.session_state.cena = "Carne"
            st.session_state.cena_img = "images/carne.jpg"
            st.session_state.step = 3
            st.rerun()

    with col3:
        st.image("images/yo.jpg", use_container_width=True)
        if st.button(" A mí"):
            st.warning("ANDA TONTO, ese es el postre!! ¡Elige bien!")

    with col4:
        st.markdown("### Otro")
        otro = st.text_input("¿Qué te apetece?", placeholder="Escribe aquí...")
        if otro:
            st.session_state.cena = otro
            st.session_state.cena_img = None
            st.session_state.step = 3
            st.rerun()


# ---------- STEP 3: ROPA ----------
elif st.session_state.step == 3:
    st.markdown(
        "<h1 style='text-align:center;'>¿Qué te gustaría más que me pusiera para nuestra cita? </h1>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/falda.jpg", use_container_width=True)
        if st.button("Falda"):
            st.session_state.ropa = "Falda"
            st.session_state.ropa_img = "images/falda.jpg"
            st.session_state.step = 4
            st.rerun()

    with col2:
        st.image("images/vestido_corto.jpg", use_container_width=True)
        if st.button("Vestido "):
            st.session_state.ropa = "Vestido corto"
            st.session_state.ropa_img = "images/vestido.jpg"
            st.session_state.step = 4
            st.rerun()

    with col3:
        st.image("images/vestido_largo.jpg", use_container_width=True)
        if st.button(" De astronauta"):
            st.session_state.ropa = "De astronauta"
            st.session_state.ropa_img = "images/astrunauta.jpg"
            st.session_state.step = 4
            st.rerun()


# ---------- STEP 4: RESUMEN ----------
elif st.session_state.step == 4:
    st.markdown(
        "<h1 style='text-align:center; color:#e60073;'>💘 CITA CONFIRMADA 💘</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>14 de febrero 🗓️</h3>",
        unsafe_allow_html=True
    )

    st.markdown("### 🍽️ Cena elegida:")
    st.markdown(f"**{st.session_state.cena}**")

    if st.session_state.cena_img:
        st.image(st.session_state.cena_img, use_container_width=True)

    st.markdown("### 👗 Lo que me pondré:")
    st.markdown(f"**{st.session_state.ropa}**")
    st.image(st.session_state.ropa_img, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.success("Nos espera una cita increíble 💕")
    st.balloons()
