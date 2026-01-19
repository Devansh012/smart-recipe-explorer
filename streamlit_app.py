import streamlit as st
import requests

st.set_page_config(page_title="Smart Recipe Explorer")

st.title("Smart Recipe Explorer")

instructions = st.text_area(
    "Enter recipe instructions",
    height=150
)

if st.button("Simplify Recipe"):
    if not instructions.strip():
        st.error("Please enter recipe instructions")
    else:
        with st.spinner("Simplifying recipe..."):
            response = requests.post(
                "https://smart-recipe-explorer-czxqb2fteyydp6wtsfmbuw.streamlit.app/ai/simplify/",  # LOCAL for now
                json={"instructions": instructions}
            )

            if response.status_code == 200:
                st.success("Simplified Recipe")
                st.write(response.json()["simplified_recipe"])
            else:
                st.error("AI service failed")
