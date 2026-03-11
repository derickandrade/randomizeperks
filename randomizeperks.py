import streamlit as st
import language_chooser
import load_data
import utils

home_page = (
    st.Page(
    page="Home.py",
    title=f"{st.session_state.home_page_name}",
    icon="🔶"))

randomize_survivor_perks_page = (
    st.Page(
        page="RandomSurvivorPerks.py",
        title=f"{st.session_state.randomize_survivor_perks_text}",
        icon="🔷"))

randomize_killer_perks_page = (
    st.Page(
        page="RandomKillerPerks.py",
        title=f"{st.session_state.randomize_killer_perks_text}",
        icon="️☠️"))

survivor_perks_info_page = (
    st.Page(
        page="SurvivorPerks.py",
        title=f"{st.session_state.survivor_perks_info_text}",
        icon="❔"))

killer_perks_info_page = (
    st.Page(
        page="KillerPerks.py",
        title=f"{st.session_state.killer_perks_info_text}",
        icon="❓"))

pages = st.navigation(
    [home_page,
     randomize_survivor_perks_page,
     randomize_killer_perks_page,
     survivor_perks_info_page,
     killer_perks_info_page])

language_chooser.choose()

load_data.load_survivor_perks()
load_data.load_killer_perks()
utils.load_cookies()

st.sidebar.selectbox(
    f"{st.session_state.select_language_text}",
    "Português Brasileiro")

pages.run()