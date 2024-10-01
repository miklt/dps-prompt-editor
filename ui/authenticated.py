import streamlit as st
from db.postgres import update_prompt_by_tipo


def visualizar_formulario():
    st.title("Prompt Editor")
    st.write(
        "Aqui você pode editar os prompts que serão usados no aplicativo principal."
    )
    prompt_recibo_acessorio = st.session_state.get("prompts")["prompt_recibo_acessorio"]
    prompt_recibo_principal = st.session_state.get("prompts")["prompt_recibo_principal"]
    prompt_recibo_compensacao = st.session_state.get("prompts")[
        "prompt_recibo_compensacao"
    ]
    id = st.session_state.get("prompts")["id"]

    with st.form("Prompts"):
        st.write("Prompt Recibo Acessório")
        prompt_ra = st.text_area(
            "Edite o prompt aqui:",
            value=prompt_recibo_acessorio,
            height=200,
            key="prompt_ra",
        )

        st.write("Prompt Recibo Principal")
        prompt_rp = st.text_area(
            "Edite o prompt aqui:",
            value=prompt_recibo_principal,
            height=200,
            key="prompt_rp",
        )

        st.write("Prompt Recibo Compensação")
        prompt_rc = st.text_area(
            "Edite o prompt aqui:",
            value=prompt_recibo_compensacao,
            height=200,
            key="prompt_rc",
        )

        submitted = st.form_submit_button("Salvar")
        if submitted:
            update_prompt_by_tipo("acessorio", prompt_ra, id)
            update_prompt_by_tipo("principal", prompt_rp, id)
            update_prompt_by_tipo("compensacao", prompt_rc, id)
            st.success("Prompt atualizado com sucesso!")
            st.session_state["prompts_updated"] = True
            st.session_state["prompts_received"] = False
        # if st.button("Salvar"):
        #     st.session_state["prompt"] = (prompt, id)
        #     update_prompt_by_tipo("acessorio",prompt, id)
        #     st.success("Prompt atualizado com sucesso!")
        #     st.session_state["prompt_updated"] = True
        #     st.session_state["prompt_received"] = False
