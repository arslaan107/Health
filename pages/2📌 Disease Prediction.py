import json

import Config as cfg
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from Config import doctor_search

def get_disease(val):
    for key, value in cfg.disease_encode_dict.items():
        if val == value:
            return key

def predict_disease(in_sym):
    lst = np.zeros(len(cfg.symptoms))
    for k in range(0, len(cfg.symptoms)):
        for s in in_sym:
            lst[k] = 1
    
    model  = joblib.load(cfg.TRAINED_MODEL_DIS)
    prediction = model.predict([lst])
    prediction = get_disease(prediction[0])
    return prediction


def split_by_pipe(value):
    """
    Splits the given text by commas and print each on new line
    """
    value_lst = value.split("|")

    return value_lst


def med_search(medicine):
    
    split_med = medicine.split(" ")
    if len(split_med) > 1:
        medicine = "+".join(split_med)
        url = f"https://www.drugs.com/search.php?searchterm={medicine}"

    url = f"https://www.drugs.com/search.php?searchterm={medicine}"

    return url

def get_precautions(disease):
    """
    Returns a list of precautions of the specified disease
    """
    prec = pd.read_csv(cfg.PRECAUTIONS_DATA)

    precautions = prec.loc[prec["Disease"] == disease].values.tolist()[0][1:]

    return precautions


def fetch_disease_info(disease=None):
    """
    Will fetch all the information of a particular disease
    """
    with open(cfg.DISEASE_DATA) as f:
        disease_data = json.load(f)

    common_name = disease_data[disease]["common name"]
    gen_overview = disease_data[disease]["Disease overview"][0].get("general_overview")
    frequency = disease_data[disease]["Disease overview"][1].get("frequency")
    gen_info = disease_data[disease]["Disease overview"][2].get("general_info")
    causes = disease_data[disease]["Disease overview"][2].get("cause")

    try:
        types = disease_data[disease]["types"]
    except:
        pass

    if types:
        disease_type = split_by_pipe(types)
    else:
        disease_type = None

    gen_info_lst = split_by_pipe(gen_info)
    symptoms = disease_data[disease]["symptoms"].replace("|", ", ")
    causes = split_by_pipe(causes)
    precautions = get_precautions(disease)
    treatment = split_by_pipe(disease_data[disease]["treatment"])
    medications = split_by_pipe(disease_data[disease]["medications"])
    specialists = split_by_pipe(disease_data[disease]["specialists"])
    more_info_link = disease_data[disease]["more info"]
    return (
        common_name,
        gen_overview,
        frequency,
        gen_info_lst,
        symptoms,
        causes,
        precautions,
        treatment,
        medications,
        specialists,
        disease_type,
        more_info_link,
    )



def disease_app():
    st.set_page_config(
        page_title ='Disease Diagnosis',
        page_icon = "🏥",
    )

    st.markdown(
        f"<h1 style='text-align: center; color: white;'>Disease Diagnosis to Treatment</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p style="font-size:22px; text-align: center; color: white;">Select the symptoms you are suffering from and the algorithm will predict the disease you are suffering from along with precautions, personalized medicine recommendations, specialists and much more.</p>',
        unsafe_allow_html=True,
    )


    st.markdown("***")

    inp_symptoms = st.multiselect("Select the symptoms: ", cfg.symptoms)

    submit = st.button("Predict")
    if len(inp_symptoms) >= 4:
        if submit:

            prediction = predict_disease(inp_symptoms)
            st.markdown(
                f"<h2 style='text-align: center; color: red;font-weight:bold;'>You are suffering from {prediction}</h2>",
                unsafe_allow_html=True,
            )
            st.write("")
            st.warning(
                "Don't panic. Read all the precautions, treatments and consult your nearest specialists if the problem worsens."
            )

            (
                common_name,
                gen_overview,
                frequency,
                gen_info_lst,
                symptoms,
                causes,
                precautions,
                treatment,
                medications,
                specialists,
                disease_type,
                more_info_link,
            ) = fetch_disease_info(prediction)

            st.markdown("---")
            st.subheader("Disease Overview 🧐")
            st.markdown(f"**Common name** : {common_name}")
            st.markdown(f"**Description**: {gen_overview}")
            st.markdown(f"**Frequency 📈**: {frequency}")
            st.markdown("---")


            st.markdown(f"🏥  {gen_info_lst[0]}")
            st.markdown(f"💊  {gen_info_lst[1]}")
            st.markdown(f"🔬  {gen_info_lst[2]}")
            st.markdown(f"🕒  {gen_info_lst[3]}")
            st.markdown("---")


            st.subheader("Causes 📝")
            for c in causes:
                st.markdown(f'👉 {c}')
            st.markdown("----")

            st.subheader("Symptoms 😷")
            st.markdown(f"{symptoms}.")
            st.markdown("---")


            st.subheader("Precautions 🩹")
            for prec in precautions:
                st.markdown(f"📌  {prec}")
            st.markdown("---")


            st.subheader("Professional Treatment 🩺")
            for t in treatment:
                st.markdown(f"- {t}")
            st.markdown("---")
            st.markdown("---")


            st.subheader("Medications 💊")
            st.write(
                "Click on the medicine name to get more info (dosage, side-effects,etc)"
            )
            for m in medications:
                meds = f"- [{m}]({med_search(m)})"
                st.markdown(meds, unsafe_allow_html=True)
            st.markdown("---")


            st.subheader("Specialists 👨‍⚕")
            st.write(
                "Click on the specialist's name to find out the nearest specialist to you ..."
            )
            for s in specialists:
                doctor = f"- [{s}]({doctor_search(s)})"
                st.markdown(doctor, unsafe_allow_html=True)
            st.markdown("---")

            st.subheader(
                f"To read more about this disease visit this [link]({more_info_link})"
            )

    else:
        st.error("Please enter atleast 4 symptomns")

if __name__ == "__main__":
    disease_app()









