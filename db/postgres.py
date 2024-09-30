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


def get_prompt():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, prompt_recibo_acessorio, prompt_recibo_principal FROM prompts order by data_alteracao desc limit 1"
    )
    prompt = cursor.fetchone()
    cursor.close()
    conn.close()
    return prompt


def update_prompt(prompt, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE prompts SET prompt_recibo_acessorio = %s, prompt_recibo_principal = %s WHERE id = %s",
        (prompt, prompt, id),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True
