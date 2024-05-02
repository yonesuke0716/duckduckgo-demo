import streamlit as st
from duckduckgo_search import DDGS

st.title("suggestions")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().suggestions("分析", region="jp-jp")

        print(results)
        """
    )

with tab2:
    if st.button("Search"):
        results = DDGS().suggestions("分析", region="jp-jp")
        st.write(results)
