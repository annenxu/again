import streamlit as st
import random

st.set_page_config(page_title="Good Luck on Your First Day Pookie", page_icon="🐢", layout="centered")

st.title("Look at you with a big boy job!")
st.markdown("I'm so proud of you and so excited that we're buying Robben Island soon")

if st.button("Click here, daddy Doerr 🙂‍↕️"):
    messages = [
        "Jokes aside, I am so so so proud of you Niki-poo.",
        "Good luck on your very first day as a full time office zaddy! I still don't know exactly what you do but those Teams emojis and Excel functions don't know what's coming today.",
        "You may not want to hear this but know that I'm praying for your joy, success and progression in this role. I believe with my whole heart He'll protect you and strengthen you.",
        "Curtis and I are thinking of you today, and love you a lot! We don't care that you're the office weirdo, we think you're cool ❤️❤️",
    ]
    message = random.choice(messages)
    st.balloons()
    st.success(message)
