# 🔐 Password Strength Meter & Generator

A Streamlit-powered web application designed to evaluate password strength in real-time and generate strong, secure passwords to protect against cyber threats.

---

## 🚀 Problem Statement

Weak and predictable passwords remain one of the primary entry points for data breaches and unauthorized system access. Many users struggle to create passwords that strike the right balance between complexity and security guidelines. This tool solves that problem by offering instant security feedback and an automated generator to craft robust passwords effortlessly.

---

## ✨ Features

- **Real-Time Password Analysis**: Evaluates password strength based on length, special characters, numerical values, and case sensitivity.
- **Custom Password Generator**: Generates strong, random passwords based on user-defined constraints.
- **Security Feedback & Tips**: Provides actionable advice on how to improve weak passwords.
- **Clean Interactive UI**: Powered by Streamlit for a smooth and intuitive user experience.

---

## 👤 Customer Interface

- **Password Tester**: Input field with real-time feedback meters (Weak, Moderate, Strong).
- **Generator Controls**: Customization toggles for length, inclusion of digits, uppercase letters, and special symbols.
- **One-Click Copy**: Fast and efficient option to generate and use secure passwords instantly.

---

## 🛠️ Admin Interface

*(Note: Designed primarily as a client-side utility app)*

- **App Settings & Parameters**: Option to configure baseline minimum complexity requirements and default generator lengths via configuration parameters.
- **Environment Management**: Isolated Python environment tracking with `pyvenv.cfg` and custom package rules.

---

## 🔗 Links

- **Live Application**: [Deploy Link Here](https://your-app-link.streamlit.app)
- **GitHub Repository**: [Repository Link](https://github.com/Abhisek-desk/Password-Strength-Meter-And-Generator)

---

## 📊 Application Workflow

```text
[ User Input ] ---> [ Password Validator Rule Engine ] ---> [ Instant Score & Tips ]
       |
       +-----------> [ Custom Criteria Options ] -----> [ Secure Password Output ]
