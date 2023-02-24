import streamlit as st
import streamlit as st
import streamlit.components.v1 as components

st.markdown(
        '<p style="font-size:22px; text-align: center; color: gold;font-size: 25px;">Our World In Data</p>',
        unsafe_allow_html=True,
    )

components.iframe(
    "https://ourworldindata.org/grapher/burden-of-disease-by-cause?time=1990..2019",
    width=1000, height=600, scrolling=True
)

components.iframe(
    "https://ourworldindata.org/grapher/burden-of-disease-by-cause",
    width=1000, height=600, scrolling=True
)


