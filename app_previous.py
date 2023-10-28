import hmac
import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# main app starts:
# Load the T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Define the available choices for task prefixes
choices = {
    "1": "translate English to German",
    "2": "cola sentence",
    "3": "summarize"
}

# Create a Streamlit web app
st.title("T5 Text Processing App")

# Let the user choose a task
user_choice = st.selectbox("Choose a task:", list(choices.values()))

# Get the user's choice
selected_task = None
for key, value in choices.items():
    if user_choice == value:
        selected_task = key

if selected_task is None:
    st.error("Please select a valid task.")
else:
    # Get the input sentences from the user
    sentences = st.text_area("Enter the text to process:")

    if st.button("Generate Output"):
        # Check the user's choice and set the task_prefix accordingly
        task_prefix = choices[selected_task]

        # Tokenize the input sentences
        input_text = f"{task_prefix}: {sentences}"
        input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

        # Generate the output based on the chosen task
        output_ids = model.generate(input_ids, max_length=100, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode and display the output
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        st.write("Generated Output:", output_text)
