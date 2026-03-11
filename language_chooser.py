import streamlit as st
import language_pt_br

def choose():
    if 'st.session_state.selected_language' not in st.session_state:
        st.session_state.selected_language = "Português Brasileiro"
    language = st.session_state.selected_language
    match language:
        case "English":
            ...
        case "Português Brasileiro":
            language_pt_br.load()