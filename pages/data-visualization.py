
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("성적 데이터 분석 및 시각화")

# 예시 성적 데이터 생성
data = {
	"이름": ["홍길동", "김철수", "이영희", "박민수", "최지우", "정수빈", "한지민", "오세훈", "유재석", "강호동"],
	"국어": np.random.randint(60, 100, 10),
	"영어": np.random.randint(60, 100, 10),
	"수학": np.random.randint(60, 100, 10)
}
df = pd.DataFrame(data)

st.subheader("원본 성적 데이터")
st.dataframe(df)

# 과목별 평균
st.subheader("과목별 평균 점수")
mean_scores = df[["국어", "영어", "수학"]].mean()
st.write(mean_scores)

# 학생별 총점 및 평균
df["총점"] = df[["국어", "영어", "수학"]].sum(axis=1)
df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1)

st.subheader("학생별 총점 및 평균")
st.table(df[["이름", "총점", "평균"]])

# 과목별 점수 분포 시각화 (matplotlib)
st.subheader("과목별 점수 분포 (히스토그램)")
fig, ax = plt.subplots()
ax.hist([df["국어"], df["영어"], df["수학"]], bins=8, label=["국어", "영어", "수학"], alpha=0.7)
ax.set_xlabel("점수")
ax.set_ylabel("학생 수")
ax.set_title("과목별 점수 분포")
ax.legend()
st.pyplot(fig)

# 학생별 평균 점수 막대그래프 (Streamlit 내장)
st.subheader("학생별 평균 점수 (막대그래프)")
st.bar_chart(df.set_index("이름")["평균"])

# 최고/최저 학생 정보
st.subheader("최고/최저 평균 학생")
max_student = df.loc[df["평균"].idxmax()]
min_student = df.loc[df["평균"].idxmin()]
st.write(f"최고 평균: {max_student['이름']} ({max_student['평균']:.2f})")
st.write(f"최저 평균: {min_student['이름']} ({min_student['평균']:.2f})")
