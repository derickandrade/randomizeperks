import streamlit as st
from streamlit import session_state


def update_filters_open_cookie(value):
    st.session_state.controller.set("filters_open", value)

def update_perks_cookie(perk, value):
    st.session_state.controller.set("perk" + perk, value)


def title_section():
    col1, col2 = st.columns([4, 1], gap='small')
    with col1:
        st.title(
            f":rainbow[{st.session_state.title}:" +
            f" {st.session_state.survivors_word}]")
    with col2:
        st.image('static/icon/survivors_icon.png', width=70)


def filters_section():
    cookie_value = st.session_state.filters_value
    value = cookie_value if cookie_value is not None else True
    with st.expander(
            f"{st.session_state.filters_word}",
            expanded=value,
            on_change=update_filters_open_cookie,
            args=[not value]):
        col1, col2 = st.columns([4, 3],
                                      gap='small')

        with col1:
            st.text(f"{st.session_state.character_word}")
            with st.container(border=True,
                              height=600):
                all_perks = st.session_state.all_survivor_perks
                if 'selected_survivor_perks' not in st.session_state:
                    st.session_state.selected_survivor_perks = []
                selected_perks = st.session_state.selected_survivor_perks
                for perk_name, perk_data in all_perks.items():
                    if 'perk' + perk_name not in session_state:
                        cookie_value = st.session_state.controller.get(
                            "perk" + perk_name)
                        st.session_state['perk' + perk_name] = (
                            cookie_value if cookie_value is not None else True)
                    selected = st.checkbox(
                        (perk_name + " - " + perk_data['character']),
                        key=("perk" + perk_name),
                        on_change=update_perks_cookie,
                        args=(perk_name, not cookie_value))
                    if selected and perk_name not in selected_perks:
                        selected_perks.append(perk_name)
                    elif not selected and perk_name in selected_perks:
                        selected_perks.remove(perk_name)


        with col2:
            st.write("")


title_section()
filters_section()