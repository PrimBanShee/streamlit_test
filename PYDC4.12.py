import streamlit as st
with st.form('Order đồ uống'):

  drinks = ('Trà sữa truyền thống', 'Trà sữa matcha', '  Trà sữa trái cây')
  option_drink = st.selectbox('Bạn muốn loại đồ uống gì?', drinks)

  sugars = ('Đường trắng', 'Đường nâu', 'Không thêm đường')
  option_sugar = st.selectbox('Bạn thích thêm loại đường nào cho đồ uống của bạn?', sugars)

  jellys = ('Thạch rau câu', 'Thạch nha đam', 'Không thêm thạch')
  option_jelly = st.selectbox('Bạn thích thêm loại thạch nào cho đồ uống của bạn?', jellys)

  nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)

  bill = {'Loại đồ uống:': option_drink, 'Loại đường:': option_sugar, 'Loại thạch:': option_jelly, 'Số lượng:': nums}
    
  submitted = st.form_submit_button("Xác nhận")
  if submitted:
    st.write('Bạn đã chọn:')
    for x,y in bill.items():
      st.write(x,y)

print_bill = st.checkbox('In hoá đơn')
if print_bill:
  ans = ''
  for x in bill:
    ans += str(x) + ' ' + str(bill[x]) + '\n'
  st.download_button('In hoá đơn', ans)