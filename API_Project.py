import streamlit as st
import sqlite3
import ollama
def FileAttachment():
   uploaded_file = st.file_uploader("Choose a file to attach", type = ["csv", "txt", "pdf"])
   if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
    st.write(file_details)
    st.success("File attached successfully!")
   else:
    print("There was an error attaching your file!")
def question():
 question = st.text_input("Would you like to attach a file (yes or no)")
 question.lower()
 if question == 'yes':
  FileAttachment()
  question()
def TextPrompt():
  Prompt = st.text_input("Enter your prompt or information: ")
def Reply():
  Reply = st.text_input("Would you like to prompt the AI?")
  Reply.lower
  if Reply == 'yes':
    TextPrompt()
summary = st.text_input("Input a general summary of the information you have researched: ")
question()
Reply()