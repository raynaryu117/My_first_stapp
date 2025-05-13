import streamlit as st # Streamlit 라이브러리 임포트

#타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기')

#텍스트 출력
st.write('# 1. markdown 텍스트 작성하기')

#Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운 목록 2-1
        - 마크다운 목록 2-2
    
    ## 마크다운 헤더2
    - [네이버](https://www.naver.com/)
    - [구글](www.google.co.kr)
    
    ### 마크다운 헤더 
    일반 텍스트
    '''
    )

#Data Frame 출력
import pandas as pd #pandas 라이브러리 임포트

st.write('#2.DataFrame 표시하기') #텍스트 출력
df = pd.DataFrame({ #DataFrame 생성
    '이름' : ['홍길동', '이순신', '강감찬'],
    '나이' : [20, 45, 35]
    })

st.dataframe(df) #DataFrame 출력

#그래프 출력
import numpy as np #numpy 라이브러리 임포트

st. dataframe(df) #텍스트 출력
chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20행 3열의 랜덤 숫자
    columns=['a', 'b', 'c']
)

# 바 차트 출력
st.bar_chart(chart_data)
st.bar_chart(chart_data) # 바 차트 출력

#이미지 출력
from PIL import Image #이미지 처리를 위한 PIL 라이브러리 임포트

st.write('#4.이미지 표시하기') #텍스트 출력
img =Image.open('python.png') #이미지 파일 열기 
st.image(img, width=300) #이미지 출력