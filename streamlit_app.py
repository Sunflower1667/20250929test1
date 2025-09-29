
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 한글 폰트 설정 (모든 matplotlib 차트에 적용)
font_path = os.path.abspath("fonts/NanumGothic-Regular.ttf")
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False

st.title("Streamlit 요소 예시")

# 텍스트 요소
st.header("텍스트 요소")
st.subheader("서브헤더 예시")
st.text("일반 텍스트 예시")
st.markdown("**마크다운** _예시_ :sparkles:")
st.code("print('Hello Streamlit!')", language='python')

# 입력 요소
st.header("입력 요소")
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이 입력", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의하십니까?")
option = st.radio("성별 선택", ["남성", "여성", "기타"])
selected = st.selectbox("좋아하는 과일", ["사과", "바나나", "오렌지"])
multi = st.multiselect("좋아하는 색상", ["빨강", "파랑", "초록", "노랑"])
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")
file = st.file_uploader("파일 업로드")

# 버튼
st.header("버튼")
if st.button("클릭!"):
    st.success("버튼이 클릭되었습니다!")

# 슬라이더
st.header("슬라이더")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.write(f"선택된 값: {value}")

# 데이터프레임/테이블
st.header("데이터프레임/테이블")
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)
st.dataframe(df)
st.table(df.head())


# 차트
st.header("차트")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# matplotlib 예시
st.header("matplotlib 차트")
fig, ax = plt.subplots()
ax.plot(df.index, df["A"], label="A 컬럼")
ax.set_title("matplotlib 라인 플롯 예시", fontproperties=fontprop)
ax.set_xlabel("Index", fontproperties=fontprop)
ax.set_ylabel("A 값", fontproperties=fontprop)
ax.legend(prop=fontprop)
st.pyplot(fig)

# 이미지
st.header("이미지")
from PIL import Image
import requests
from io import BytesIO
img_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png"
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
st.image(img, caption="Streamlit 로고", use_column_width=True)

# 알림/메시지
st.header("알림/메시지")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")

# 진행바
st.header("진행바")
import time
progress = st.progress(0)
for i in range(1, 101):
    time.sleep(0.01)
    progress.progress(i)
st.write("진행 완료!")

# 사이드바
st.sidebar.title("사이드바 예시")
st.sidebar.write("여기에 사이드바 내용을 추가할 수 있습니다.")
