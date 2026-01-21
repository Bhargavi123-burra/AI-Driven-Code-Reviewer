import streamlit as st

#st.header('AI Driven Code Reviewer')
#st.subheader('Paste your code below')
#st.text_area('Code Editor area', height=350,placeholder='paste your code here')
#if st.button('Analyzer'):
    #st.write('hello')

from code_parser import parse_code
from style_checker import show_style_corrected
from error_detector import detect_errors
from ai_suggester import get_ai_suggestion

st.title("AI Code Reviewer")
code = st.text_area("Code: ")

if st.button("Analysis"):
    if code:
        result = parse_code(code)
        result1 = show_style_corrected(code)
        if result["success"]:
            st.success("Parsed!")
            st.code(result1, language="python")
        else:
            st.error(result["error"]["message"])
    else:
        st.warning("Please enter some code first!")