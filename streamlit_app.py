
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit 페이지 제목 설정
st.title("Sin and Cos Function Visualization")

# 파라미터 입력 받기
x_start = st.slider('X 시작값', 0.0, 10.0, 0.0)
x_end = st.slider('X 종료값', 10.0, 20.0, 10.0)

# x 값 생성
x = np.linspace(x_start, x_end, 1000)

# y 값 생성
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y_sin, label='sin(x)')
ax.plot(x, y_cos, label='cos(x)')
ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sin and Cos Functions')

# Streamlit을 통해 그래프 출력
st.pyplot(fig)


@st.cache
def expensive_computation(x):
    return np.sin(x) + np.cos(x)

# 캐시된 함수 호출
result = expensive_computation(x)

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increment'):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
