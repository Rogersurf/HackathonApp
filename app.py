import streamlit as st

def main():
    st.title("My First Streamlit App")

    # Adding a text input widget
    user_input = st.text_input("Enter your name", "Type Here...")

    if st.button('Say Hello'):
        st.write(f'Hello, {user_input}!')

if __name__ == "__main__":
    main()