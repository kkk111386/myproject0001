import streamlit as st
st.title('나의 첫 스트림릿 프로젝트')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요:', ['딸기빙수','아이스크림'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 반가워요!!')
