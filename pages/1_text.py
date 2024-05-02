import streamlit as st
from duckduckgo_search import DDGS

st.title("text")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().text("Python プログラミング", region="jp-jp", max_results=3)
        print(results)
        """
    )
    st.info("日本語の検索結果を取得する場合は、region='jp-jp'を指定します。")
    st.info("max_resultsで取得する検索結果の数を指定できます。")

with tab2:
    if st.button("Search"):
        results = DDGS().text("Python プログラミング", region="jp-jp", max_results=3)
        st.write(results)
