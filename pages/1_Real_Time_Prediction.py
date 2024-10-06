import streamlit as st
from Home import Face_Rec
from streamlit_webrtc import webrtc_streamer
import av
import time
# import Face_Rec
# st.set_page_config(page_title='Face Recognition')

st.subheader('Real Time Face Pridiction')



with st.spinner("Loading Data"):
    redis_face_db = Face_Rec.retrive_data(name='academy:register')
    st.dataframe(redis_face_db)

st.success("Data Loaded Successfully")

#Real Time Pridiction

waitTime = 30
setTime = time.time()
realtimepred = Face_Rec.RealTimePred()


def video_frame_callback(frame):
    global setTime
    img = frame.to_ndarray(format="bgr24")

    pred_img = realtimepred.face_prediction(img,redis_face_db,'facial_features',['Name','Role'],thresh=0.5)

    timenow = time.time()
    difftime = timenow-setTime

    if difftime >= waitTime:
        realtimepred.saveLogs_db()
        setTime = time.time()

        print('Save data to database')
    return av.VideoFrame.from_ndarray(pred_img,format="bgr24")

webrtc_streamer(key="realtimePrediction",video_frame_callback=video_frame_callback,
                 rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    })