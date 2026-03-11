import streamlit as st

def load():
    # "Survivors Perks"
    st.session_state.survivor_perks_text = "Vantagens de Sobrevivente"

    # "Killers Perks"
    st.session_state.killer_perks_text = "Vantagens de Assassino"

    # app.py
    # "Select a Language"
    st.session_state.select_language_text = "Selecione uma língua"

    # "Home"
    st.session_state.home_page_name = "Início"

    # home.py:
    # "Randomize Perks"
    st.session_state.title = "Randomizar Vantagens"

    # "Select one option:"
    st.session_state.header = "Selecione uma opção:"

    # "Survivors"
    st.session_state.survivors_word = "Sobreviventes"

    # "Filters"
    st.session_state.filters_word = "Filtros"

    # "Character"
    st.session_state.character_word = "Personagem"

    # "Perks"
    st.session_state.perks_word = "Vantagens"

    # "Randomize Survivor Perks"
    st.session_state.randomize_survivor_perks_text = (
        "Randomizar Vantagens de Sobrevivente")

    # "Randomize Survivor Perks"
    st.session_state.randomize_killer_perks_text = (
        "Randomizar Vantagens de Assassino")

    # "Survivor Perks Info"
    st.session_state.survivor_perks_info_text = (
        "Vantagens de Sobrevivente Info")

    # "Killer Perks Info"
    st.session_state.killer_perks_info_text = (
        "Vantagens de Assassino Info")

load()