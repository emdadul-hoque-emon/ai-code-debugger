import streamlit as st
from PIL import Image

from api_call import generate_note
st.set_page_config(page_title="AI Code Debugger", page_icon=":brain:", layout="centered")


st.title("AI Code Debugger",anchor=False)
st.write("AI Code Debugger is a tool that helps you debug your code by providing hints and solutions with code snippets.")

with st.container(border=True):
    image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], help="Upload an image file (jpg, jpeg, png) to display it in the main area.")

    selected_type = st.selectbox("Select a type", 
                                 ["Hints", "Solutions with code"], 
                                 help="Select the type of content you want to see: 'Hints' for helpful tips or 'Solutions with code' for detailed solutions including code snippets.",
                                  index=None
                                 )
    clicked = st.button("Solution with code", help="Click to submit your selection and see the results based on the selected type.")
if clicked:
    if selected_type and image:
        with st.spinner(f"Generating {selected_type.lower()} of the image..."):
          pill_image = Image.open(image)
          result = generate_note(pill_image, selected_type)
          st.markdown(result)
    else:
        st.error("Please select a type and upload an image to see the results.")