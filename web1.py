
import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to Streamlit!")
st.write("copyright")


st.title("This is a title")           # Largest text
st.header("This is a header")         # Large header
st.subheader("This is a subheader")   # Medium header
st.write("This is regular text")      # General purpose writing
st.markdown("This is markdown")   # Markdown support
st.text("This is plain text")         # Fixed-width text
st.code("print('Hello World')")       # Code block
st.latex(r"\frac{1}{2}")              # LaTeX equations

st.success("Success message!")
st.error("Error message!")
st.warning("Warning message!")
st.info("Information message")

st.sidebar.title("Sidebar Title")
st.sidebar.write("This is in the sidebar")

import streamlit as st
st.title("Input Widgets Example") 
     
name = st.text_input("Enter your name") 
age = st.number_input("Enter your age", min_value=0, max_value=120, value=30) 
is_happy = st.checkbox("Are you happy?") 
color = st.selectbox("Choose your favorite color", ["Red", "Green", "Blue"]) 
     
if st.button("Submit"):
    st.write(f"Name: {name}") 
    st.write(f"Age: {age}") 
    st.write(f"Happy: {'Yes' if is_happy else 'No'}") 
    st.write(f"Favorite color: {color}")