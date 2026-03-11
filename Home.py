import streamlit as st

st.title(f":rainbow[{st.session_state.title}]")
st.header(f"{st.session_state.header}")
left_column, right_column = st.columns(2, vertical_alignment="center")

survivor_perks_selected = left_column.button(
    f"{st.session_state.survivor_perks_text}", width=150)
killer_perks_selected = right_column.button(
    f"{st.session_state.killer_perks_text}", width=150)

if survivor_perks_selected:
    survivor_perks_selected = False
    st.switch_page("RandomSurvivorPerks.py")

if killer_perks_selected:
    killer_perks_selected = False
    st.switch_page("RandomKillerPerks.py")