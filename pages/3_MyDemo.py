import streamlit as st
import pandas as pd
import numpy as np

# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="홍정환 데모 스트림릿 배포하기",
    layout="wide",
)

st.header('서울특별시 공공자전거 일별대여건수')
st.subheader("CSV 파일업로드")
st.text('1단계 : 서울열린데이터광장에서 데이터셋을 CSV 파일 다운로드후 DataFrame생성')

# 파일 업로드 위젯 설정
uploaded_file = st.file_uploader('choose a file')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame 생성')
    st.write(df)
    st.subheader('요약 통계량 추출')
    st.write(df.describe())
else:
    st.info('Upload a csv file')
    
# Markdown 연습
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.header("https://docs.streamlit.io/")
st.markdown("[Document](#https://docs.streamlit.io/)")


# chat_message 연습
# with st.chat_message("user"):
#     st.write("Hello 👋")
#     st.line_chart(np.random.randn(30, 3))
    
# chat_input 연습
# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
    

# select box 연습

st.title("Selectbox")

contact_options = ["Email", "Phone", "Text"]

st.header("Selectbox from a list")

contact_selected = st.selectbox("How would you like to be contacted?",
                                options= contact_options)

st.write("Selectbox returns:", contact_selected,
         "of type", type(contact_selected))

if contact_selected == "Email":
    st.write("**Comfirm your email address by clicking the link sent to you**")
else:
    st.write("**Thank you, we will be in touch soon**")

st.header("Selectbox from a NumPy array")

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

col1, mid, col2 = st.columns([1, 0.1, 3])
with col1:
    st.write("My Array:")
    array

array_selection = st.selectbox("Choose an option", options = array, index=1)

st.write("Array selection returns:", array_selection,
         "of type", type(array_selection))


if "submitted" not in st.session_state:
    st.session_state.submitted = False

text1 = st.text_input("Username")
text2 = st.text_input("Password", type="password")

if (st.button("Login") or st.session_state.submitted) and text1=="admin" and text2=="password":
    st.session_state.submitted = True
    st.success("Welcome!")

    if st.button("Plot Graph"):
        st.session_state.submitted = False
        chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])
        st.area_chart(chart_data)
        
        
        