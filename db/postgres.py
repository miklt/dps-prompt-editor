import psycopg2
import streamlit as st
import json


# Function to connect to the database
def get_connection():
    conn = psycopg2.connect(
        host=st.secrets["db_host"],
        database=st.secrets["db_name"],
        user=st.secrets["db_user"],
        password=st.secrets["db_password"],
        port=st.secrets["db_port"],
    )
    return conn


def get_prompts():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, prompt_recibo_acessorio, prompt_recibo_principal, prompt_recibo_compensacao, prompt_nfe FROM prompts order by data_alteracao desc limit 1"
        )
        prompt = cursor.fetchone()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    if prompt is None:
        return None
    else:
        r = {
            "id": prompt[0],
            "prompt_recibo_acessorio": prompt[1],
            "prompt_recibo_principal": prompt[2],
            "prompt_recibo_compensacao": prompt[3],
            "prompt_nfe": prompt[4],
        }
        return r


def update_prompt_by_tipo(tipo_recibo, prompt, id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if tipo_recibo == "principal":
            cursor.execute(
                "UPDATE prompts SET prompt_recibo_principal = %s WHERE id = %s",
                (prompt, id),
            )
        elif tipo_recibo == "acessorio":
            cursor.execute(
                "UPDATE prompts SET prompt_recibo_acessorio = %s WHERE id = %s",
                (prompt, id),
            )
        elif tipo_recibo == "compensacao":
            cursor.execute(
                "UPDATE prompts SET prompt_recibo_compensacao = %s WHERE id = %s",
                (prompt, id),
            )
        elif tipo_recibo == "nfe":
            cursor.execute(
                "UPDATE prompts SET prompt_nfe = %s WHERE id = %s",
                (prompt, id),
            )
        conn.commit()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return True
