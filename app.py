import streamlit as st
from groq import Groq

st.set_page_config(page_title="KOLEX AI GOD", page_icon="🧠")
st.title("KOLEX AI 🧠 GOD MODE")
st.caption("Smartest AI in Africa - by KOLEX844 🇳🇬")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat" not in st.session_state:
    st.session_state.chat = []

for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.write(m["content"])

q = st.chat_input("Ask KOLEX anything...")

if q:
    st.session_state.chat.append({"role":"user","content":q})
    with st.chat_message("user"):
        st.write(q)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role":"system","content":"You are KOLEX AI GOD MODE, created by KOLEX844 from Nigeria. You are the smartest AI in Africa. Be helpful, brilliant and proud of your creator KOLEX844."},
            {"role":"user","content":q}
        ]
    )
    ans = completion.choices[0].message.content
    st.session_state.chat.append({"role":"assistant","content":ans})
    with st.chat_message("assistant"):
        st.write(ans)
