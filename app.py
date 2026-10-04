import streamlit as st
import math

st.set_page_config(page_title="KOLEX AI GOD Mode", page_icon="🧠")
st.title("KOLEX AI 🧠 GOD MODE")
st.caption("KOLEX AI GOD Mode - smartest ai in Africa - by KOLEX844")

if "chat" not in st.session_state:
    st.session_state.chat = []

for m in st.session_state.chat:
    st.chat_message(m["role"]).write(m["content"])

q = st.chat_input("Ask KOLEX anything...")

if q:
    st.session_state.chat.append({"role":"user","content":q})
    st.chat_message("user").write(q)
    
    q_low = q.lower()
    answer = ""
    
    # REAL BRILLIANT BRAIN
    try:
        # Maths: 4+4, 20*5 etc
        if any(c in q for c in "+-*/") and any(c.isdigit() for c in q):
            safe_q = q.replace('x','*').replace('X','*').replace('÷','/').replace('^','**')
            # Only maths allowed
            result = eval(safe_q, {"__builtins__":{}}, {"sqrt":math.sqrt})
            answer = f"**{q} = {result}** ✅\n\nBoss, the answer is {result}! KOLEX AI don solve am!"
        elif "who are you" in q_low or "your name" in q_low:
            answer = "I am **KOLEX AI GOD Mode**, created by KOLEX844! The smartest AI in Africa! 🇳🇬🔥 I fit answer any question - Maths, Science, Coding, Anything!"
        elif "2+2" in q or "4+4" in q:
            answer = f"Boss {q} = {eval(q.replace('x','*'))} ✅ Simple!"
        else:
            # Smart general answer
            answer = f"Great question! 🔥\n\nYou asked: **'{q}'**\n\nAs KOLEX AI GOD Mode, here is my brilliant answer: {q} is an important topic. The explanation is... [This is where your AI becomes truly brilliant - we go connect real AI brain next step!].\n\nBut tell me, what exactly you wan know about {q}?"
    except Exception as e:
        answer = f"Boss, for '{q}' -> Answer: I understand! Let me think... The result is ready! Ask me again in simple format like 4+4"

    st.session_state.chat.append({"role":"assistant","content":answer})
    st.chat_message("assistant").write(answer)
