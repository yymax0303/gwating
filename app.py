import streamlit as st
from db import init_db
from utils import load_css

st.set_page_config(page_title="과팅 매칭", page_icon="💘", layout="centered")
load_css()
init_db()

st.markdown("""
<div class="hero">
    <h1>💘 과팅 매칭 시스템</h1>
    <p>AI가 최적의 짝을 찾아드려요! 왼쪽 메뉴에서 페이지를 선택하세요.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 사용 방법
1. **👤 참가자 등록** — 참가자들이 설문을 작성해요
2. **🤖 AI 매칭** — 주최자가 매칭을 실행해요
3. **💑 매칭 결과** — 결과를 확인하고 채팅해요
""")