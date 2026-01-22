import streamlit as st
import time
from code_parser import parse_code
from style_checker import show_style_corrected
from error_detector import detect_errors
from ai_suggester import get_ai_suggestions

def stream_data(text):
    """Yields text word by word for the typewriter effect."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

st.set_page_config(
    page_title="AI Code Reviewer Application",
    page_icon="😇",
    layout="wide"
)

st.logo("logo.png", size="large")
st.title("AI Code Reviewer")

if st.button("Refresh"):
    st.rerun()

tab1, tab2 = st.tabs(["Code Suggested", "AI Suggestions"])

# ---------------- TAB 1 ----------------
with tab1:
    st.markdown("Paste your Python code below and click **Analyze** to get feedback on errors and style.")

    code = st.text_area("Code Input:", height=200)

    if st.button("Analyze", type="primary"):
        if not code.strip():
            st.warning("Please enter some code first!")
        else:
            parse_result = parse_code(code)
            if not parse_result["success"]:
                st.error("Your code has syntax errors!")
                st.code(parse_result["error"]["message"])
                st.stop()

            st.success("Code parsed successfully!")

            # -------- ERROR DETECTION --------
            st.subheader("🛑 Error Detection Results")
            error_result = detect_errors(code)

            if error_result["success"]:
                if error_result["error_count"] == 0:
                    st.info("No static errors found! Your code looks clean.")
                else:
                    st.warning(f"Found {error_result['error_count']} potential issue(s):")
                    for error in error_result["errors"]:
                        with st.expander(f"{error['type']}", expanded=True):
                            st.write(f"**Message:** {error['message']}")
                            st.info(f"**Suggestion:** {error['suggestion']}")
            else:
                st.error("Could not analyze code for errors")

            # -------- STYLE CHECK --------
            st.subheader("🎨 Style-Corrected Version")
            try:
                style_result = show_style_corrected(code)
                if style_result["success"]:
                    with st.expander("View Formatted Code"):
                        st.code(style_result["corrected_code"], language="python")
                        st.caption("This uses PEP8 standards to format your code.")
                else:
                    st.info("Style correction not available.")
            except Exception:
                st.info("Style checking module not found.")

            # -------- ORIGINAL CODE --------
            st.caption("Reference: Your Original Input")
            with st.expander("See Original Code"):
                st.code(code, language="python")


# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("🤖 AI Improvement Suggestions")

    if 'code' in locals() and code.strip():
        suggestions = get_ai_suggestions(code)

        for suggestion in suggestions:
            with st.chat_message("assistant"):
                st.write(suggestion)
    else:
        st.info("Please enter and analyze code in Code Suggested tab first.")
