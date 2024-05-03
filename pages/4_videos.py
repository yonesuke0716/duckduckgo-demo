import streamlit as st
from duckduckgo_search import DDGS

st.title("videos")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().videos(
            keywords="cars",
            region="jp-jp",
            safesearch="moderate",
            timelimit="w",
            resolution="high",
            duration="medium",
            max_results=5,
        )

        print(results)
        """
    )

with tab2:
    if st.button("Search"):
        st.write("実行結果")
        results = DDGS().videos(
            keywords="cars",
            region="jp-jp",
            safesearch="moderate",
            timelimit="w",
            resolution="high",
            duration="medium",
            max_results=1,
        )
        st.write(results)
        st.video(results[0]["content"])
