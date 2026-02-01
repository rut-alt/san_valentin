import streamlit as st
import random
import os

st.set_page_config(page_title="💘 San Valentín 💘", layout="centered")

# -------- FUNCION SEGURA PARA IMÁGENES --------
def show_image(path):
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning(f"No se encuentra la imagen: {path}")

# ---------- ESTADOS ----------
st.session_state.setdefault("step", 1)
st.session_state.setdefault("no_position", random.randint(0, 2))
st.session_state.setdefault("cena", None)
st.session_state.setdefault("cena_img", None)
st.session_state.setdefault("ropa", None)
st.session_state.setdefault("ropa_img", None)

# ---------- STEP 1: CITA ----------
if st.session_state.step == 1:
    st.markdown(
        "<h1 style='text-align:center; color:#e60073;'>"
        "¿Quieres una cita conmigo el 14 de febrero? 💖"
        "</h1>",
        unsafe_allow_html=True
    )

    if st.button("💘 SÍ 💘"):
        st.session_state.step = 2
        st.rerun()

    cols = st.columns(3)
    if cols[st.session_state.no_position].button("NO"):
        st.session_state.no_position = random.randint(0, 2)
        st.rerun()

# ---------- STEP 2: CENA ----------
elif st.session_state.step == 2:
    st.markdown("<h1 style='text-align:center;'>¿Qué te gustaría cenar?</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        show_image("images/sushi.jpg")
        if st.button("Sushi"):
            st.session_state.cena = "Sushi"
            st.session_state.cena_img = "images/sushi.jpg"
            st.session_state.step = 3
            st.rerun()

    with col2:
        show_image("images/carne.jpg")
        if st.button("Carne"):
            st.session_state.cena = "Carne"
            st.session_state.cena_img = "images/carne.jpg"
            st.session_state.step = 3
            st.rerun()

    with col3:
        show_image("images/yo.pjg.jpg")
        if st.button("A mí"):
            st.warning("ANDA TONTO 😂 ese es el postre!! ¡Elige bien!")

    with col4:
        otro = st.text_input("Otro (escribe lo que quieras)")
        if otro:
            st.session_state.cena = otro
            st.session_state.cena_img = None
            st.session_state.step = 3
            st.rerun()

# ---------- STEP 3: ROPA ----------
elif st.session_state.step == 3:
    st.markdown(
        "<h1 style='text-align:center;'>¿Qué te gustaría que me pusiera para nuestra cita? </h1>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        show_image("images/falda.jpg")
        if st.button("Falda"):
            st.session_state.ropa = "Falda"
            st.session_state.ropa_img = "images/falda.jpg"
            st.session_state.step = 4
            st.rerun()

    with col2:
        show_image("images/vestido.jpg")
        if st.button("Vestido"):
            st.session_state.ropa = "Vestido"
            st.session_state.ropa_img = "images/vestido.jpg"
            st.session_state.step = 4
            st.rerun()

    with col3:
        show_image("images/astronauta.jpg")
        if st.button("Astronauta"):
            st.session_state.ropa = "Astronauta"
            st.session_state.ropa_img = "images/astronauta.jpg"
            st.session_state.step = 4
            st.rerun()

# ---------- STEP 4: RESUMEN ----------
elif st.session_state.step == 4:
    st.markdown(
        "<h1 style='text-align:center; color:#e60073;'>💘 CITA CONFIRMADA 💘</h1>",
        unsafe_allow_html=True
    )

    st.markdown("<h3 style='text-align:center;'>14 de febrero 🗓️</h3>", unsafe_allow_html=True)

    st.markdown("### 🍽️ Cena elegida:")
    st.write(st.session_state.cena)

    if st.session_state.cena_img:
        show_image(st.session_state.cena_img)

    st.markdown("### 👗 Outfit elegido:")
    st.write(st.session_state.ropa)
    show_image(st.session_state.ropa_img)

    st.success("Nos espera una cita increíble 💕")
    st.balloons()

