import streamlit as st

import base64
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="👩",
)





st.markdown("<h1 style='text-align: center;'>Welcome to the Diabetes and Cardiovascular Disease Prediction System! 👋</h1>", unsafe_allow_html=True)


st.markdown(
    """
    This a disease prediction web application,which predicts if you're under the risk of the following:
        
        
        
        1.Cardiovascular Disease
        2.Diabetes
        
    
        Please make sure to refer to a proper doctor after the prediction tests.
        These results are not meant to be a diagnosis. 
        You can meet with a doctor  to get a diagnosis and medications. 

"""
)