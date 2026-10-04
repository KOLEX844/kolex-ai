import streamlit as st

st.set_page_config(page_title="KOLEX AI", page_icon="🔥")

st.title("🔥 KOLEX AI - GOD MODE")
st.subheader("Smartest AI in Africa 🌍")

st.markdown("---")

user_input = st.text_input("Ask KOLEX anything:", placeholder="Type here...")

if user_input:
    st.success(f"KOLEX says: You asked '{user_input}' - GOD Mode activated! 🚀")
    st.balloons()

st.info("Created by KOLEX844 | Live for everyone!")
