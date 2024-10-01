import streamlit as st
from ui.authenticated import visualizar_formulario
from db.postgres import get_prompts
from ui.login import login


if "prompts_updated" not in st.session_state:
    st.session_state["prompts_updated"] = False

if "prompts_received" not in st.session_state:
    st.session_state["prompts_received"] = False

if "prompts" not in st.session_state:
    st.session_state["prompts"] = None

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False


if not st.session_state["prompts_received"]:
    prompts = get_prompts()
    print(prompts)
    if prompts is not None:
        st.session_state["prompts"] = prompts
        st.session_state["prompts_received"] = True

st.title("Aplicativo de Atualização de Prompt")


if st.session_state["authenticated"]:

    visualizar_formulario()
else:
    login()
