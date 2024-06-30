import streamlit as st

def main():
    st.title("Shashi App")
    st.write("This is a simple Streamlit application.")

    # Add a slider
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write(f"The selected value is {slider_value}")

    # Add some other components
    st.text_input("Enter some text")
    st.button("Click me")

if __name__ == "__main__":
    main()
