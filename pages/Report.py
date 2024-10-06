from Home import st
from Home import Face_Rec
st.set_page_config(page_title='Reports',layout='wide')

st.subheader('Face Pridiction Reports')

name = 'attendance:logs'
def load_logs(name,end = -1):
    logs_list = Face_Rec.r.lrange(name,start=0,end=end)
    return logs_list

tab1,tab2 = st.tabs(['Registred Data','Logs'])
with tab1:
    if st.button('Refresh Data'):
    
        with st.spinner("Loading Data"):
            redis_face_db = Face_Rec.retrive_data(name='academy:register')
            st.dataframe(redis_face_db[['Name','Role']])

with tab2:

    if st.button('Refresh_Logs'):

        st.write(load_logs(name=name))

