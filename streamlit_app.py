import streamlit as st
from ui.authenticated import visualizar_formulario
from db.postgres import get_prompt
from ui.login import login


if "prompt_updated" not in st.session_state:
    st.session_state["prompt_updated"] = False

if "prompt_received" not in st.session_state:
    st.session_state["prompt_received"] = False

if "prompt" not in st.session_state:
    st.session_state["prompt"] = None

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False


if not st.session_state["prompt_received"]:
    prompt = get_prompt()
    print(prompt)

    if prompt is not None:
        st.session_state["prompt"] = (prompt[1], prompt[0])
        st.session_state["prompt_received"] = True

st.title("Aplicativo de Atualização de Prompt")


if st.session_state["authenticated"]:

    visualizar_formulario()
else:
    login()
