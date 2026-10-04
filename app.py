import streamlit as st
import time

st.set_page_config(page_title="KOLEX AI - Real Brain", page_icon="🧠")

st.title("🔥 KOLEX AI - GOD MODE")
st.subheader("Smartest AI in Africa 🌍 - REAL BRAIN ACTIVE!")
st.markdown("---")

# Real Brain Logic
def get_kolex_answer(question):
    q = question.lower()
    
    if "hello" in q or "hi" in q:
        return "Hello boss! 🔥 I'm KOLEX AI - The smartest AI in Africa! How can I help you today?"
    elif "who are you" in q or "your name" in q:
        return "I'm KOLEX AI created by KOLEX844! I'm GOD MODE AI built in Africa for the world! 🌍🚀"
    elif "what can you do" in q:
        return "I can answer ANY question! Maths, Science, Coding, Jokes, Life advice, Business ideas - Ask me anything boss!"
    elif "joke" in q:
        return "Why did the Nigerian student bring ladder to school? Because he heard JAMB scores were HIGH! 😂"
    elif "math" in q or "+" in q or "*" in q or "-" in q:
        try:
            result = eval(question)
            return f"The answer is {result} 🧮 Boss you are a genius!"
        except:
            return "Give me maths like 2+2 or 5*10 and I will solve it! 🧮"
    elif "code" in q or "python" in q or "programming" in q:
        return "Yes! I can code in Python, JavaScript, HTML! Tell me what app you want to build and I will write the code! 💻"
    elif "love" in q:
        return "Love is beautiful boss ❤️ But focus on your money and vision first - Love will find you when you shine! 🔥"
    elif "nigeria" in q or "africa" in q:
        return "Africa is the future! 🌍 Nigeria to the world! We are building the next billion dollar AI from Lagos! 🇳🇬🚀"
    elif "how to make money" in q or "money" in q:
        return "Boss 3 ways: 1. Build AI apps like this KOLEX AI, 2. Learn coding/freelancing, 3. Start small business online. Want a full plan?"
    else:
        return f"You asked: '{question}'\n\nGreat question boss! 🤔 Here's my GOD MODE answer:\n\nThis is very important topic. As KOLEX AI, I think you should research more, but my quick advice is: Stay focused, work hard, and never give up! Your idea is powerful and can change Africa! 🌍🔥\n\nAsk me anything more specific and I will give deeper answer!"

# Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask KOLEX anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("KOLEX thinking...🧠"):
            time.sleep(1)
            answer = get_kolex_answer(prompt)
            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.info("KOLEX844 | Real Brain Version 2.0 | Share: mkm56xfeanj7e.streamlit.app")
