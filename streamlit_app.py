import streamlit as st
st.title("🎈 mimin project 1")
st.header("Bagaimana pengalamanmu menggunakan website ini?")
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
import streamlit as st
import streamlit as st

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

import pandas as pd

from datetime import datetime
import streamlit as st

st.balloons()
import streamlit as st

st.snow()

import streamlit as st
import random

st.set_page_config(page_title="Mystery Box Challenge", page_icon="🎁")

st.title("🎁 Mystery Box Challenge")
st.write("Pilih kotak misteri dan kumpulkan skor sebanyak mungkin!")

if "score" not in st.session_state:
    st.session_state.score = 0

hadiah = [
    ("💰 Kamu menemukan 10 koin!", 10),
    ("⭐ Bonus 20 poin!", 20),
    ("💎 Harta karun! +50 poin", 50),
    ("😱 Kehilangan 15 poin!", -15),
    ("💣 Jebakan! -30 poin", -30),
]

st.metric("Skor Saat Ini", st.session_state.score)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎁 Kotak 1"):
        pesan, poin = random.choice(hadiah)
        st.session_state.score += poin
        st.success(pesan)

with col2:
    if st.button("🎁 Kotak 2"):
        pesan, poin = random.choice(hadiah)
        st.session_state.score += poin
        st.success(pesan)

with col3:
    if st.button("🎁 Kotak 3"):
        pesan, poin = random.choice(hadiah)
        st.session_state.score += poin
        st.success(pesan)

st.divider()

if st.button("🔄 Reset Game"):
    st.session_state.score = 0
    st.rerun()

if st.session_state.score >= 200:
    st.balloons()
    st.success("🏆 Selamat! Kamu berhasil mencapai 200 poin!")

