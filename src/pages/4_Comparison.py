import streamlit as st
import openai_connection
import os


st.title("Document Comparison")
if "comparison_prompt" not in st.session_state:
    st.session_state.comparison_prompt = "You are an AI assistant that compares two markdown documents"

view_prompt = st.checkbox("View Prompt", value=False)
if view_prompt:
    st.session_state.comparison_prompt = st.text_area("Current Prompt", st.session_state.comparison_prompt)

output_folder = "markdown_output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

markdown_files = [f for f in os.listdir("markdown_output") if f.endswith(".md")]
selected_files = st.multiselect("Choose two markdown files to compare:", markdown_files, max_selections=2)
if len(selected_files) == 2:
    with open(os.path.join("markdown_output", selected_files[0]), "r", encoding="utf-8") as f:
        markdown_content_1 = f.read()
    with open(os.path.join("markdown_output", selected_files[1]), "r", encoding="utf-8") as f:
        markdown_content_2 = f.read()
    
    st.text_area("Document Content 1", markdown_content_1, height=200)
    st.text_area("Document Content 2", markdown_content_2, height=200)
    
    if st.button("Compare"):
        comparison = openai_connection.compare(markdown_content_1, markdown_content_2)
        st.write(comparison)  
    