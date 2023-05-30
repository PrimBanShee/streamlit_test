import streamlit as st

st.title('Điền thông tin giới thiệu bản thân em')
my_bar = st.progress(0)

quiz = ['Họ và tên:', 'Ngày tháng năm sinh:', 'Sở thích:']
answers = []
len_quiz = len(quiz)

for i in range(len_quiz):
  answer = st.text_input(quiz[i], '')
  if answer != '':
    answers.append(answer)
  if st.button('Confirm', key=str(i)):
    my_bar.progress(int(100* (len(answers)/len_quiz)))
    
if len(answers) == len_quiz:
  my_bar.progress(100)
  st.balloons()

for i in range(len(answers)):
  st.write(quiz[i], answers[i])  
