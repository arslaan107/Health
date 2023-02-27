import streamlit as st
import streamlit as st
import streamlit.components.v1 as components
import bar_chart_race as bcr

import pandas as pd
import numpy as np


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

df = pd.read_csv('./data/graph1.csv')

df.columns = [
    'Country',
    'Ctry_code',
    'Year',
    'Self_harm',
    'Forces_of_Nature',
    'Terrorism_conflict',
    'Interpersonal_violence',
    'Neglected_Tropical_Disease',
    'Substance_use',
    'Skin_diseases',
    'Enteric_infections',
    'Diabetes_kidney_diseases',
    'Cardiovascular_diseases',
    'Digestive_diseases',
    'Nutritional_deficiencies',
    'Respinf_and_TB',
    'Neonatal_disorders',
    'Chronic_respiratory_diseases',
    'Oth_non-communicable_diseases',
    'Maternal_disorders',
    'Unintentional_injuries',
    'Musculoskeletal_disorders',
    'Neoplasms',
    'Mental_disorders',
    'Neurological_disorders',
    'AIDS_STI',
    'Transport_injuries',
    'Sensory_organ_disease'
    
]

st.markdown("---")

c = ['India','Pakistan','China','Bangladesh','Russia']

select2 = st.selectbox("Select a country",c)

st.write(select2)

df_coun = df.query("Country == @select2 ")

#st.write(df_ind)
st.dataframe(data = df_coun)


@st.cache_data
def data_change(d):
    d['Year'] = d['Year'].astype(str)
    columns = ['Country','Ctry_code']
    d = d.drop(columns, axis=1)
    d['Year'] = pd.to_datetime(d['Year'])
    df_test = d.set_index('Year')
    
    return df_test

x = data_change(df_coun)

st.write("Preprocessed data")

st.dataframe(data = x)



components.html(
    bcr.bar_chart_race(
        df=x, title="Diseases", n_bars=10
    ).data
)







