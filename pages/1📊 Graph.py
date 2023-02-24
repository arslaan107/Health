import streamlit as st
import streamlit as st
import streamlit.components.v1 as components


st.sidebar.info(
        "**About**: Disease related graphs"
    )

st.markdown(
        '<p style="font-size:22px; text-align: center; color: gold;font-size: 25px;">Our World In Data</p>',
        unsafe_allow_html=True,
    )

list = ['World-wide', 'test']

select = st.selectbox("Select an option", list)


if select == 'World-wide':
    components.iframe(
    "https://ourworldindata.org/grapher/burden-of-disease-by-cause?time=1990..2019",
    width=1000, height=600, scrolling=True
)
else:
    components.iframe(
    "https://ourworldindata.org/grapher/burden-of-disease-by-cause",
    width=1000, height=600, scrolling=True
)







