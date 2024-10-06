import streamlit as st
# import onnx
# import onnxruntime
# from onnx.onnx_cpp2py_export import ONNX_ML

st.set_page_config(page_title='Attendance System',layout='wide')
st.header('Attendance System Using Face Recognition')
# import Face_Rec

with st.spinner("Loading Connections"):
        
    # Retrive Data from DB
    import Face_Rec


st.success("Loaded Sucessfully")