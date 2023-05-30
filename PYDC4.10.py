import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)
col6, col7 = st.columns([2,1])

with col1:
  b1 = st.button('Con mèo')
with col2:
  b2 = st.button('Con chó')
with col3:
  b3 = st.button('Con khỉ')
with col4:
  b4 = st.button('Đại bàng')
with col5:
  b5 = st.button('Con gà')

if b1:
  with col6:
    st.write('Âm thanh')
    audio = open('PYDC4.10/PYDC4.10 sound/cat.wav', 'rb')
    st.audio(audio, format='audio/wav')

    st.write('Video')
    video = 'https://www.youtube.com/watch?v=W86cTIoMv2U'
    st.video(video, format='video/mp4')
  with col7:
    image = 'PYDC4.10/PYDC4.10 pic/cat.jpg'
    st.image(image, caption='Con mèo')
    
if b2:
  with col6:
    st.write('Âm thanh')
    audio = open('PYDC4.10/PYDC4.10 sound/dog.wav', 'rb')
    st.audio(audio, format='audio/wav')

    st.write('Video')
    video = 'https://www.youtube.com/watch?v=zb9l63Nm9zU'
    st.video(video, format='video/mp4')
  with col7:
    image = 'PYDC4.10/PYDC4.10 pic/dog.jpg'
    st.image(image, caption='Con chó')
    
if b3:
  with col6:
    st.write('Âm thanh')
    audio = open('PYDC4.10/PYDC4.10 sound/monkey.wav', 'rb')
    st.audio(audio, format='audio/wav')

    st.write('Video')
    video = 'https://www.youtube.com/watch?v=icd_ob8UWgQ'
    st.video(video, format='video/mp4')
  with col7:
    image = 'PYDC4.10/PYDC4.10 pic/monkey.jpg'
    st.image(image, caption='Con khỉ')
    
if b4:
  with col6:
    st.write('Âm thanh')
    audio = open('PYDC4.10/PYDC4.10 sound/eagle.wav', 'rb')
    st.audio(audio, format='audio/wav')

    st.write('Video')
    video = 'https://www.youtube.com/watch?v=1ryv1u2yXCk'
    st.video(video, format='video/mp4')
  with col7:
    image = 'PYDC4.10/PYDC4.10 pic/eagle.jpg'
    st.image(image, caption='Đại bàng')
    
if b5:
  with col6:
    st.write('Âm thanh')
    audio = open('PYDC4.10/PYDC4.10 sound/chicken.wav', 'rb')
    st.audio(audio, format='audio/wav')

    st.write('Video')
    video = 'https://youtu.be/SNSr8ti3Y4A'
    st.video(video, format='video/mp4')
  with col7:
    image = 'PYDC4.10/PYDC4.10 pic/chicken.jpg'
    st.image(image, caption='Con gà')