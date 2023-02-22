import streamlit as st
import streamlit as st

def home():
    st.set_page_config(
        page_title="Home",
        page_icon="👨‍⚕️",
    )
    st.sidebar.info(
        "**About**: This project is made using publicly available data and comes with no gaurantee. We do not store any of the patient's personal information."
    )

    # st.markdown(f"<h1 style='text-align: center; color: blue; font-size: 50px;'>Healthify</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        st.image("assets/HEALTH.png")

    with col3:
        st.write("")
    # st.image("logo/logo.png")

    st.markdown(
        '<p style="font-size:22px; text-align: center; color: white;font-size: 25px;">Improving Healthcare, Improving Lives, Bridging the gap between technology and health</p>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    st.markdown(
        f"<h2 style='text-align: center; color: yellow; background-color: purple;'>About the website</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown(
        f"<p style='text-align: center; color: white; font-size: 20px'>💠 We use state-of-the-art machine learning and deep learning techologies to provide you with your own virtual Health Consultant</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<p style='text-align: center; color: white; font-size: 20px'>💠 We provide digital health and healthcare solutions to help common people and health organizations power their care experience and improve health outcomes with advanced analytics</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        f"<h2 style='text-align: center; color: yellow; background-color: purple;'>Our Services</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown(
        f"⚕️ **Disease Diagnosis** - Enter the symptoms you are suffering from and you will get to know the disease you are suffering from, precautions to take, medications and specialists near you to cure the disease"
    )
    st.markdown(
        f"⚕️ **Early Diabetes Detection** - Enter the patients attributes from the test report and check whether he/she have chances of diabetes or not"
    )

    st.markdown(
        f"⚕️ **Liver Disease Detection** - Enter the patients attributes from the test report and check whether he/she have chances of any type of liver disease or not"
    )

    st.markdown("---")

    st.warning(
        "**Disclaimer**: This is a testing site...Please consult a real doctor in case of symptoms"
    )





if __name__ == "__main__":
    home()