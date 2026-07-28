# 🔐 Interactive Password Strength Meter & Generator

An interactive, user-friendly Streamlit web application designed to evaluate password strength in real time and generate customizable, highly secure passwords to protect against cyber threats.

---

## 🚀 Problem Statement

Weak, short, and predictable passwords are among the most common vulnerabilities exploited in cybersecurity breaches. Users often struggle to gauge whether their passwords satisfy essential security criteria or fail to generate complex passwords manually. This tool provides an immediate visual analysis of password complexity and offers an automated generator to produce strong, randomized passwords on demand.

---

## ✨ Features

- **Real-Time Password Evaluation**: Evaluates passwords out of a 5-point criteria scale using regular expressions (`re`).
- **Visual Progress Bar**: Displays a dynamic percentage-based progress bar reflecting overall security strength.
- **Detailed Security Breakdown**: Shows real-time checkmarks (✅) and crosses (❌) for specific security rules (length, casing, digits, special characters).
- **Customizable Password Generator**: Generates randomized passwords varying from 8 to 30 characters.
- **Granular Character Toggles**: Allows users to include or exclude uppercase, lowercase, numbers, and special symbols.

---

## 👤 Customer Interface

The application features a tabbed navigation system for a seamless user experience:

1. **Password Strength Meter Tab**:
   - **Input Box**: Masked text input field for secure typing.
   - **Interactive Feedback**: Dynamic color-coded alerts (`Strong`, `Good`, `Moderate`, `Weak`) with matching score indicators.
   - **Checklist**: Live criteria checklist for minimum length (8+ chars), uppercase, lowercase, numbers, and special characters.

2. **Password Generator Tab**:
   - **Length Slider**: Adjust password length dynamically between 8 and 30 characters.
   - **Options**: Checkboxes for Uppercase, Lowercase, Numbers, and Special Characters.
   - **Code Output**: Instant generation rendered in a standard code box for easy one-click copying.

---

## 🛠️ Admin Interface

*(Client-side utility application)*

- **Tabbed Layout Management**: Native Streamlit `st.tabs` state management without persistent server logs.
- **Input Validation**: Edge-case protection (displays an error if no character sets are selected during password generation).
- **Environment Isolation**: Tracked Python virtual environment via `pyvenv.cfg` and explicit dependency declarations in `requirements.txt`.

---

## 🔗 Links

- **Live Application**: [Streamlit App Link](https://your-app-link.streamlit.app) *(Replace with actual link)*
- **GitHub Repository**: [Repository Link](https://github.com/Abhisek-desk/Password-Strength-Meter-And-Generator)

---

## 📊 Application Workflow

```text
                     +---------------------------------------+
                     |           User Input (Tabs)           |
                     +-------------------+-------------------+
                                         |
            +----------------------------+----------------------------+
            |                                                         |
            v                                                         v
  [ Tab 1: Strength Meter ]                                 [ Tab 2: Generator ]
            |                                                         |
  Evaluate 5 Regex Criteria                                Build Custom Charset Pool
  (Length, Upper, Lower, Digit, Symbol)                     (Upper, Lower, Digit, Symbol)
            |                                                         |
  Calculate Score (0 - 5)                                   Generate Random String
            |                                                         |
  Render Progress & Feedback                                Render Copyable Code Box
