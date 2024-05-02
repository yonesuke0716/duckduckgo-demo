import streamlit as st
from duckduckgo_search import DDGS

st.title("images")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().images(
            keywords="トヨタ",
            region="jp-jp",
            safesearch="moderate",
            size=None,
            color="Monochrome",
            type_image=None,
            layout=None,
            license_image=None,
            max_results=5,
        )

        print(results)
        """
    )
    with st.expander("See explanation"):
        st.info("keywordsで検索キーワードを指定します。(日本語でも大丈夫です。)")
        st.info("safesearchで検索結果の安全性を指定できます。on | moderate | off")
        st.info("日本語の検索結果を取得する場合は、region='jp-jp'を指定します。")
        st.info("max_resultsで取得する検索結果の数を指定できます。")

with tab2:
    if st.button("Search"):
        results = DDGS().images(
            keywords="トヨタ",
            region="jp-jp",
            safesearch="moderate",
            size=None,
            color="Monochrome",
            type_image=None,
            layout=None,
            license_image=None,
            max_results=1,
        )
        st.write(results)
        st.image(results[0]["image"], caption="image")
        st.image(results[0]["thumbnail"], caption="thumbnail")
