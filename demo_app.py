import streamlit as st

from code_parser import parse_code
from demo_style_checker import show_style_corrected
from error_detector import detect_errors

st.title("AI Code Reviewer")
st.markdown("Paste your Python code below and click Analyze!")

code = st.text_area("Code:")

if st.button("Analyze"):
    if not code:
        st.warning("Please enter some code first!")
    else:
        st.info("Analyzing your code...")

        # ======================================
        # STEP 1: Parse the code
        # (Function) def parse_code(code_string: Any) -> dict[str, Any]
        # Parses python code into AST
        # ======================================

        parse_result = parse_code(code)

        if not parse_result["success"]:
            # If parsing fails, show error and STOP
            st.error("Your code has syntax errors!")
            st.code(parse_result["error"]["message"])
            st.stop()  # Stop here, don't continue

        # If we reach here, parsing was successful
        st.success("Code parsed successfully!")

        # ======================================
        # STEP 2: Check for errors (unused variables)
        # ======================================

        st.subheader("Error Detection Results")

        error_result = detect_errors(code)  # call the FUNCTION

        if error_result["success"]:
            if error_result["error_count"] == 0:
                st.success("No errors found! Your code looks good.")
            else:
                st.warning(f"Found {error_result['error_count']} issue(s).")

                # Show each error
                for error in error_result["errors"]:
                    with st.expander(f"{error['type']}", expanded=True):
                        st.write(f"**Message:** {error['message']}")
                        st.info(f"**Suggestion:** {error['suggestion']}")
        else:
            st.error("Could not analyze code for errors.")

        # ======================================
        # STEP 3: Check style (if you have this module)
        # ======================================

        st.subheader("Style Corrected Version")

        try:
            style_result = show_style_corrected(code)

            if style_result["success"]:
                st.code(style_result["corrected_code"], language="python")
                st.caption("This is how your code looks with proper formatting")
            else:
                st.info("Style correction not available")

        except Exception as e:
            st.info("Style checking module not found")

        # ======================================
        # STEP 4: Show original code for comparison
        # ======================================

        st.subheader("Your Original Code")
        st.code(code, language="python")
