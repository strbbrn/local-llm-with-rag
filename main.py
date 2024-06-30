import streamlit as st

def main():
    st.title("Shashi App")
    st.subheader("Checkboxes")
    if st.checkbox("Show/hide text"):
        st.write("You've chosen to show some text!")

    # Add selectbox
    st.subheader("Selectbox")
    option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {option}")

    # Add file
    st.subheader("File Uploader")
    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'csv'])
    if uploaded_file is not None:
        st.write("File details:")
        st.write(uploaded_file.name)
        st.write(uploaded_file.size)
        st.write("File content:")
        st.write(uploaded_file.read())

    # Add a button
    if st.button("Click me"):
        st.write("Button clicked!")

if __name__ == "__main__":
    main()
