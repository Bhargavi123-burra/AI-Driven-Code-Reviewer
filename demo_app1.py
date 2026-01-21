import streamlit as st
from code_parser import parse_code
from error_detector import detect_errors
from demo_style_checker import clean_code
from demo_ai_suggester import get_ai_suggestion

st.set_page_config(
    page_title="AI Code Reviewer application",
    page_icon="image.png",
    layout="wide"
)
st.image("image.png",width=100)

#Title
st.title("Code Reviewer")

#Get code
code = st.text_area("Paste your code:")
tab1, tab2 = st.tabs(["Home", "Dashboard"])
with tab1:
    st.write("Home content")
with tab2:
    st.write("Dashboard content")

#Analyze button
if st.button("Analyze"):
    if code:
        #Find errors
        errors = detect_errors(code)
        for err in errors:
            st.subheader("Unused_variables")
            st.error(err)
        
        #Step 4: Get AI suggestions
        ai_suggestions = get_ai_suggestion(code)
        st.subheader("AI Suggestion")
        for suggestion in ai_suggestions:
            st.info(suggestion["message"])
    else:
        st.warning("Enter code first!")  
    if st.button(" Refresh"):
        st.rerun  