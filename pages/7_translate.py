import streamlit as st
from duckduckgo_search import DDGS

st.title("translate")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().translate("機械学習", to="en")

        print(results)
        """
    )

with tab2:
    if st.button("Search"):
        results = DDGS().translate("機械学習", to="en")
        st.write(results)
