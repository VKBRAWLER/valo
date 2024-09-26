import streamlit as st
from PIL import Image
import easyocr
import numpy as np
st.title("OCR and Keyword Search")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    reader = easyocr.Reader(['en', 'hi'])  # Specify languages
    results = reader.readtext(np.array(image))
    extracted_text = ""
    for (bbox, text, prob) in results:
        extracted_text += text + " "
    plain_txt = extracted_text
    search_keyword = st.text_input("Enter keyword to search in the extracted text")
    if search_keyword != "":
        if search_keyword in extracted_text:
            extracted_text = extracted_text.replace(search_keyword, f"<mark style='background-color: yellow;'>{search_keyword}</mark>")
            st.success(f"Keyword '{search_keyword}' found in the extracted text!")
        else:
            st.error(f"Keyword '{search_keyword}' not found in the extracted text.")
    st.subheader("Extracted Text")
    st.write(extracted_text, unsafe_allow_html=True)
    # st.download_button(
    #     label="Download Extracted Text",
    #     data=plain_txt,
    #     file_name="extracted_text.txt",
    #     mime="text/plain"
    # )