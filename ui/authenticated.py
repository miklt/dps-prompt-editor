import streamlit as st
from db.postgres import update_prompt


def visualizar_formulario():
    st.title("Prompt Editor")
    st.write("Aqui você pode editar o prompt que será exibido no aplicativo principal.")
    prmpt = st.session_state.get("prompt")[0]
    id = st.session_state.get("prompt")[1]
    print(prmpt, id)
    prompt = st.text_area("Edite o prompt aqui:", value=prmpt, height=200)

    if st.button("Salvar"):
        st.session_state["prompt"] = (prompt, id)
        update_prompt(prompt, id)
        st.success("Prompt atualizado com sucesso!")
        st.session_state["prompt_updated"] = True
        st.session_state["prompt_received"] = False
