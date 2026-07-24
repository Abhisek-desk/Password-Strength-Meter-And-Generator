import streamlit as st
import re
import random
import string


st.set_page_config(
    page_title="Password Strength Meter & Generator",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Interactive Password Strength Meter & Generator")

tab1, tab2 = st.tabs(["Password Strength Meter", "Password Generator"])

with tab1:

    st.subheader("Evaluate Your Password")
    password = st.text_input(
        "Type or Paste Your Password Below:",
        type="password",
        key="pwd_input"
    )

    if password:
        # Rule Evaluations using regex and string check
        len_ok = len(password) >= 8
        upper_ok = bool(re.search(r"[A-Z]", password))
        lower_ok = bool(re.search(r"[a-z]", password))
        digit_ok = bool(re.search(r"\d", password))
        spchar_ok = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
        # Compute overall score out of 5
        score = sum([len_ok, upper_ok, lower_ok, digit_ok, spchar_ok])

        st.markdown("### Security Analysis")
        st.markdown("### Strength")
        progress_val=score/5
        st.progress(progress_val,text=f'Strength Score:{score}/5({int(progress_val*100)}%)')

        st.write("✅ Minimum 8 Characters" if len_ok else "❌ Minimum 8 Characters")
        st.write("✅ Contains Uppercase Letter" if upper_ok else "❌ Contains Uppercase Letter")
        st.write("✅ Contains Lowercase Letter" if lower_ok else "❌ Contains Lowercase Letter")
        st.write("✅ Contains Number" if digit_ok else "❌ Contains Number")
        st.write("✅ Contains Special Character" if spchar_ok else "❌ Contains Special Character")


        if score == 5:
            st.success("🟢 Strong Password (100%)")
        elif score == 4:
            st.info("🟢 Good Password (80%)")
        elif score == 3:
            st.warning("🟡 Moderate Password (60%)")
        else:
            st.error("🔴 Weak Password")
    else:
        st.info('Please Enter A Password Above to See Its Security Breakdown.')

# Tab 2 : Password Generator
with tab2:

    st.subheader("Generate a Secure Password")

    length = st.slider(
        "Password Length",
        min_value=8,
        max_value=30,
        value=12
    )

    include_upper = st.checkbox("Include Uppercase Letters", value=True)
    include_lower = st.checkbox("Include Lowercase Letters", value=True)
    include_digits = st.checkbox("Include Numbers", value=True)
    include_special = st.checkbox("Include Special Characters", value=True)

    if st.button("Generate Password"):
        characters = ""

        if include_upper:
            characters += string.ascii_uppercase
        if include_lower:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        if characters == "":
            st.error("Please select at least one character type.")
        else:
            password = "".join(random.choice(characters) for _ in range(length))

            st.success("Generated Password")
            st.code(password)
            st.info("Copy and use this password securely.")