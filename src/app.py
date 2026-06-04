import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Configuration
st.set_page_config(
    page_title="The Gulabi Lounge",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Load your files
def load_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

html_code = load_file("index.html")
css_code = load_file("style.css")
js_code = load_file("script.js")

# 3. Combine them
# We inject CSS into <style> and JS into <script> within the HTML
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        {css_code}
        /* Fix for Streamlit container */
        body {{ margin: 0; padding: 0; }}
        .stMarkdown {{ padding: 0; }}
    </style>
</head>
<body>
    {html_code}
    <script>
        {js_code}
    </script>
</body>
</html>
"""

# 4. Render the HTML/CSS/JS
# height=1000 ensures your content isn't cut off. Adjust as needed.
components.html(full_html, height=1000, scrolling=True)

# 5. Optional: Add a Native Streamlit Form for Membership
# Since HTML forms don't submit data, we add a real Python form at the bottom
st.divider()
st.header("🌸 Join The Gulabi Lounge Community")
st.write("Ready to start your journey? Sign up for membership below.")

with st.form("membership_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    interest = st.selectbox("Interested In", ["Workshops", "Membership", "Both"])
    submitted = st.form_submit_button("Become a Member")

    if submitted:
        st.success(f"Welcome {name}! We will contact you at {email} shortly.")
        # Here you would normally connect to a database or Google Sheet
        # st.write(f"Data: {name}, {email}, {interest}")
