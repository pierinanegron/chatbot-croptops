import streamlit as st 
from chatbot import ChatBotCroptops

st.set_page_config(
    page_title="NAVARROTEX ChatBot",
    page_icon="logo.png",
    layout="centered"
)

col1, col2, col3 = st.columns([0.3, 2, 0.3])
with col2:
    st.image("logo.png", width=400)

st.markdown("<p style='text-align: center; color: gray;'>ChatBot de Atención al Cliente</p>", unsafe_allow_html=True)

if 'chatbot' not in st.session_state:
    st.session_state.chatbot = ChatBotCroptops('intents.json')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f"**👤 tu:** {message['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {message['content']}")

st.divider()
col1,col2 = st.columns([4, 1])

with col1:
    usuario_input = st.text_input(
        "Escribe tu pregunta",
        placeholder="Ej: ¿Cuanto Cuesta?"
    )

with col2:
    boton_enviar = st.button("Enviar")

if boton_enviar and usuario_input:
    st.session_state.messages.append({
        'role': 'user',
        'content': usuario_input
    })

    respuesta, intent = st.session_state.chatbot.obtener_respuesta(usuario_input)

    st.session_state.messages.append({
        'role': 'bot',
        'content': respuesta
    })

    st.rerun()

st.divider()
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "NAVARROTEX © 2024 | ChatBot Inteligente 24/7"
    "</p>",
    unsafe_allow_html=True
)