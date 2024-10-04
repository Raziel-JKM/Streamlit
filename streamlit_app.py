# Streamlit을 활용한 시각화 및 웹 배포 교안

## 1. Streamlit 개요
Streamlit은 Python을 사용하여 대화형 웹 애플리케이션을 빠르고 쉽게 개발할 수 있는 프레임워크입니다. 데이터 시각화와 분석 결과를 웹을 통해 배포하는 데 유용하며, 간단한 Python 코드만으로 웹 페이지를 만들 수 있습니다.

- **장점**: 간단한 문법으로 대화형 컴포넌트 구성 가능
- **사용 사례**: 데이터 시각화, 대화형 데이터 대시보드, 머신러닝 모델 결과 공유 등

## 2. Streamlit을 이용한 시각화
Streamlit을 사용하면 matplotlib, numpy 등을 사용하여 만든 그래프를 웹 페이지로 쉽게 배포할 수 있습니다. 예시로, numpy를 이용해 sin과 cos 그래프를 그려보고 웹으로 배포하는 예제를 다뤄보겠습니다.

## 3. 실습: Sin, Cos 그래프 시각화 및 배포
### 3.1 코드 작성
아래의 코드는 numpy와 matplotlib을 사용하여 sin과 cos 그래프를 생성하고, 이를 Streamlit을 통해 웹 페이지로 배포하는 코드입니다.

```python
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
```

### 3.2 주요 기능 설명
- **st.title()**: 웹 페이지 제목 설정
- **st.slider()**: 사용자가 직접 값을 선택할 수 있도록 슬라이더 추가
- **np.linspace()**: 지정된 범위에서 일정한 간격의 x 값 생성
- **plt.subplots()**: matplotlib을 사용해 그래프 생성
- **st.pyplot()**: Streamlit 페이지에 matplotlib 그래프 표시

### 3.3 코드 실행 및 배포
이 코드를 Streamlit에서 실행하여 로컬에서 웹 앱을 테스트하고, Streamlit Cloud에 배포해봅니다.

```bash
streamlit run app.py
```

## 4. Streamlit Cloud 배포하기
Streamlit Cloud를 사용하면 간단하게 애플리케이션을 배포할 수 있습니다.

1. **GitHub에 코드 업로드**: 먼저 GitHub에 코드를 업로드합니다.
2. **Streamlit Cloud 로그인**: https://share.streamlit.io에 접속하여 GitHub 계정으로 로그인합니다.
3. **Deploy**: 저장소를 선택하고 배포를 클릭합니다. 이후 앱이 자동으로 배포됩니다.

## 5. 캐시 처리
Streamlit에서 데이터나 계산 결과를 캐시하여 실행 속도를 높일 수 있습니다. 이를 위해 `st.cache` 데코레이터를 사용합니다.

```python
@st.cache
def expensive_computation(x):
    return np.sin(x) + np.cos(x)

# 캐시된 함수 호출
result = expensive_computation(x)
```
- **@st.cache**: 시간이 오래 걸리는 연산을 캐시하여 다음에 호출할 때 속도를 향상시킵니다.

## 6. Session 관리
Streamlit에서는 사용자별로 다른 세션을 관리할 수 있습니다. 예를 들어, 사용자가 선택한 슬라이더 값이나 입력값은 세션마다 고유하게 저장됩니다. Streamlit의 session_state를 사용하여 상태를 유지할 수 있습니다.

```python
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increment'):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
```
- **st.session_state**: 각 세션의 상태를 저장하고 관리하는 데 사용됩니다.#
