import json
import streamlit as st
from PIL import Image


@st.cache_data
def load_survivor_perks():
    with open("static/data/survivor_perks.json") as file:
        survivor_perks = json.load(file)
    st.session_state['all_survivor_perks'] = survivor_perks


@st.cache_data
def load_killer_perks():
    with open("static/data/killer_perks.json") as file:
        killer_perks = json.load(file)
    st.session_state['all_killer_perks'] = killer_perks

