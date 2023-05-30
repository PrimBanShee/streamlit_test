import streamlit as st
import time
import random

st.title('Đố vui toán học')
my_bar = st.progress(100)

for percent_complete in range(100, 0, -1):
     time.sleep(0.1)
     my_bar.progress(percent_complete - 1)