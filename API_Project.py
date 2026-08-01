import streamlit as st
prompt = input("Input a general summary of the information you have researched: ")
def question():
 global question; input("Would you like to attach a file (yes or no)")
 question.lower()
def FileAttachment():
  uploaded_file = st.file_uploader("Choose a file to attach", type=["csv", "txt", "pdf"])
  if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
    st.write(file_details)
    st.success("File attached successfully!")
question()
while question == 'yes' or 'y':
  FileAttachment()
  question()