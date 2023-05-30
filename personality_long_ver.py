import streamlit as st

st.set_page_config(page_title='Trắc nghiệm tính cách', page_icon=':question:', layout='wide')

st.title('Hãy chọn một con vật bạn yêu thích')
col1, col2, col3, col4, col5 = st.columns(5)

Personality = {'Con mèo':'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát được đi nghỉ. Mong muốn kéo dài thời gian nghỉ ngơi đang áp đảo lý trí của bạn. Thậm chí bạn chỉ muốn kết thúc ngày làm việc nhanh chóng để trở về nhà, ngồi trên chiếc ghế bành ấm cúng, nghỉ ngơi, thư giãn và đọc sách hoặc xem chương trình truyền hình yêu thích.', 'Con chó':'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề xảy ra. Tinh thần làm việc cao là tốt. Nhưng hãy xem xét nhiệm vụ trước mắt một cách cẩn thận để xem liệu bạn có thể giải quyết nó một mình được hay không. Những người xung quanh có thể thay đổi kế hoạch của họ và điều này sẽ ảnh hưởng đến bạn nếu cần đến sự giúp đỡ từ ai đó.', 'Con sư tử': 'Nếu sư tử là con vật đầu tiên bạn thấy trong bài trắc nghiệm vui đoán tính cách này, có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng. Mọi người ngưỡng mộ bạn nhưng cũng có thể ghen tị bởi lúc nào cũng thấy bạn tỏa sáng hoặc đôi lúc cư xử hơi kiêu ngạo. Vì vậy, hãy đối xử với mọi người một cách bình đẳng để giá trị bản thân được nâng cao hơn.', 'Con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn. Có lẽ công việc đang quá mệt mỏi hoặc bản thân không chịu được môi trường làm việc hiện tại. Bình tĩnh là điều cần nhất cho bạn lúc này. Mọi người đều muốn nghỉ ngơi, nhưng để có được sự tự do xứng đáng thì bạn cần phải thể hiện sự bền bỉ và hiệu quả công việc tốt.', 'Thiên nga':'Bạn đang yêu. Đó là lý do tại sao mọi thứ xung quanh bạn đều có vẻ tuyệt vời, bao gồm cả những người khó tính hay càu nhàu bạn nhất. Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó cho đến khi bạn cảm thấy có thể đối diện với những bước ngoặt tiếp theo.'}

with col1:
  b1 = st.button('Con mèo')
with col2:
  b2 = st.button('Con chó')
with col3:
  b3 = st.button('Con sư tử')
with col4:
  b4 = st.button('Con ngựa')
with col5:
  b5 = st.button('Thiên nga')
      
if b1:
  with st.expander('Con mèo'):
    st.write(Personality['Con mèo'])
if b2:
  with st.expander('Con chó'):
    st.write(Personality['Con chó'])
if b3:
  with st.expander('Con sử tử'):
    st.write(Personality['Con sư tử'])
if b4:
  with st.expander('Con ngựa'):
    st.write(Personality['Con ngựa'])
if b5:
  with st.expander('Thiên nga'):
    st.write(Personality['Thiên nga'])

with st.sidebar:
  st.title('Trắc nghiệm tính cách')
  if b1:
    st.write('Con vật bạn chọn là con mèo')
  if b2:
    st.write('Con vật bạn chọn là con chó')
  if b3:
    st.write('Con vật bạn chọn là con sư tử')
  if b4:
    st.write('Con vật bạn chọn là con ngựa')
  if b5:
    st.write('Con vật bạn chọn là thiên nga')