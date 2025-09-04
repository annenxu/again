
import streamlit as st
import random

st.set_page_config(page_title="Niklas's Luck", page_icon="🍀", layout="centered")

st.title("Does Nik get some today? 🤪")
st.markdown("Are you lucky or not 😇!")

if st.button("Ask Noks"):
    answer = random.choice(["Yes, baby 🥰", "Womp Womp"])

    if answer == "Yes, baby 🥰":
        st.balloons()
        st.success(f"The Oracle says: **{answer}!** 🎉")
    else:
        st.error(f"The Oracle says: **{answer}.** 😢")

st.info("Disclaimer: TThis is binding between Nik and Noks")
