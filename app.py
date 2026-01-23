import streamlit as st
import time
from code_parser import parse_code
from style_checker import show_style_corrected
from error_detector import detect_errors
from ai_suggester import get_ai_suggestions

# Typewriter effect (optional)
def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🧠",
    layout="wide"
)

st.image("logo.png", width=150)
st.title("AI Code Reviewer")

if st.button("Refresh"):
    st.rerun()

tab1, tab2 = st.tabs(["Code Review", "AI Suggestions"])

# --- TAB 1: CODE REVIEW ---
with tab1:
    code = st.text_area("Paste your Python code here:", height=250)

    if st.button("Analyze", key="analyze"):
        if not code.strip():
            st.warning("Please enter some Python code first!")
        else:
            # Syntax parse
            parse_res = parse_code(code)
            if not parse_res["success"]:
                st.error("Syntax Error!")
                st.code(parse_res["error"]["message"])
                st.stop()
            st.success("Parsed Successfully")

            # Static Errors
            st.subheader("Static Error Detection")
            err = detect_errors(code)
            if err["success"]:
                if err["error_count"] == 0:
                    st.success("No errors found.")
                else:
                    for e in err["errors"]:
                        with st.expander(e["message"]):
                            st.write(e["suggestion"])
            else:
                st.error("Error detection failed.")

            # Style Correction
            st.subheader("Style Correction")
            style = show_style_corrected(code)
            if style["success"]:
                st.code(style["corrected_code"], language="python")
            else:
                st.info("Style checker failed.")

# --- TAB 2: AI SUGGESTIONS ---
with tab2:
    st.subheader("🤖 AI Improvement Suggestions")

    if not code.strip():
        st.info("Please analyze code in the first tab.")
    else:
        suggestions = get_ai_suggestions(code)

        if isinstance(suggestions, list):
            for suggestion in suggestions:
                st.success(suggestion)
        else:
            st.error("AI suggestions failed to load.")

