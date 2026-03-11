import streamlit as st
from streamlit_cookies_controller import CookieController

def load_cookies():
    if 'controller' not in st.session_state:
        controller = CookieController()
        st.session_state.controller = controller

    cookies = st.session_state.controller.getAll()
    for cookie_name, cookie_value in cookies.items():
        if cookie_name not in st.session_state:
            st.session_state[cookie_name] = cookie_value

    if 'excluded_survivor_perks' not in st.session_state:
        cookie_list = st.session_state.controller.get(
            'excluded_survivor_perks')
        if cookie_list is not None:
            st.session_state.excluded_survivor_perks = cookie_list
        else:
            st.session_state.excluded_survivor_perks = []

    if 'filters_value' not in st.session_state:
        cookie_value = st.session_state.controller.get(
            'filters_value')
        value = cookie_value if cookie_value is not None else True
        st.session_state.filters_value = value