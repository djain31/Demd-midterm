from flask import Flask, flash, request
import streamlit as st
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

pickled_model = open("pickle_iris_model.pkl","rb")
classifier  = pickle.load(pickled_model)

def hello():   
    try:
        st.title("Wine Quality Check")
        f1 = st.text_input("f1")
        f2 = st.text_input("f2")
        f3 = st.text_input("f3")
        f4 = st.text_input("f4")
        f5 = st.text_input("f5")
        f6 = st.text_input("f6")
        f7 = st.text_input("f7")
        f8 = st.text_input("f8")
        f9 = st.text_input("f9")
        f10 = st.text_input("f10")
        f11 = st.text_input("f11")
        f12 = st.text_input("f12")
        f13 = st.text_input("f13")    
        result = classifier.predict([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13])
        if st.button("Enter"):
            st.success(result)  
    except Exception as e:
        return f"Error occurred with message : {e}"

if __name__ == "__main__":
    hello()


