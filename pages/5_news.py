import streamlit as st
from duckduckgo_search import DDGS

st.title("news")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().news(
            keywords="円安",
            region="jp-jp",
            safesearch="moderate",
            timelimit="m",
            max_results=2,
        )

        print(results)
        """
    )

with tab2:
    if st.button("Search"):
        results = DDGS().news(
            keywords="円安",
            region="jp-jp",
            safesearch="moderate",
            timelimit="m",
            max_results=2,
        )
        st.write(results)
