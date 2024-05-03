import streamlit as st
from duckduckgo_search import DDGS

st.title("answer")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().answers("Japan")

        print(results)
        """
    )
    with st.expander("引数に関する補足"):
        st.warning(
            "引数に日本語を与えても検索結果がうまく返ってこないため、使用する場合は英語を与えましょう。"
        )

with tab2:
    if st.button("Search"):
        results = DDGS().answers("Japan")
        st.write(results)
