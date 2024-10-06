# from Home import st
import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av
from Home import Face_Rec


# st.set_page_config(page_title='Registration')
st.subheader('Registration of Face Pridiction')

registrationForm = Face_Rec.RegistrationForm()

person_name = st.text_input(label='Name',placeholder='Enter Your Name')
role = st.selectbox(label='Select Your Role', options=('Developer',
                                                       'Tech Lead',
                                                       'Tester',
                                                       'DevopsEng'))


def video_callback_func(frame):
    img = frame.to_ndarray(format='bgr24')
    reg_img,embedding = registrationForm.get_embedding(img)

    if embedding is not None:
        with open('face_embedding.txt',mode='ab') as f:
            np.savetxt(f,embedding)

    return av.VideoFrame.from_ndarray(reg_img,format='bgr24')

webrtc_streamer(key='registration',video_frame_callback=video_callback_func,
                 rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    })


if st.button('Submit'):
    return_val = registrationForm.save_data_in_db(person_name,role)
    if return_val == True:
        st.success(f"{person_name} registred sucessfully")
    elif return_val == 'name_false':
        st.error('Please enter the name : Name canot be the empty')
    elif return_val == 'file_false':
        st.error('face_embedding.txt is not found')
    
    # st.write(f'Persone Name = ',person_name)
    # st.write(f'Your Role = ',role)


