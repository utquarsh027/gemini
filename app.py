import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image

API_KEY="AIzaSyAo9yfpvJACfzgxPyX3cj3FkSoV4wUy3nY"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Generate story", 
                   page_icon="📸",
                   layout="centered",
                   initial_sidebar_state='collapsed')

def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Gemini Vision', 'Gemini Pro', 'Contact'))

    if page=="Gemini Vision":
        st.header("Gemini Vision")
        uploaded_file = st.file_uploader("Upload an Image file", accept_multiple_files=False, type=['jpg', 'png'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)

            st.image(image, caption='Uploaded Image', use_column_width=True)
            bytes_data = uploaded_file.getvalue()

        prompt=st.text_input("Enter a prompt")

        generate=st.button("Generate")
        if generate:
            try:
                model = genai.GenerativeModel('gemini-pro-vision')
                response = model.generate_content(
                glm.Content(
                    parts = [
                        glm.Part(text=prompt),
                        glm.Part(
                            inline_data=glm.Blob(
                                mime_type='image/jpeg',
                                data=bytes_data
                            )
                        ),
                    ],
                ),
                stream=True)

                response.resolve()
                st.write(response.text)
            except:
                st.write("Error!Check the prompt or uploaded image")

    elif page=="Gemini Pro":
        model = genai.GenerativeModel('gemini-pro')
        prompt=st.text_area("Enter your input")
        generate=st.button("Generate")
        if generate:
            try:
                response = model.generate_content(
                glm.Content(
                    parts = [
                        glm.Part(text=prompt),
                    ],
                ))

                st.write(response.text)
            except:
                st.write("Error!Check the prompt")


if __name__ == '__main__':
    main()

