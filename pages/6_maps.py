import streamlit as st
from duckduckgo_search import DDGS

st.title("maps")

tab1, tab2 = st.tabs(["コード", "実行結果"])

with tab1:
    st.write("実行結果")
    st.code(
        """
        from duckduckgo_search import DDGS

        results = DDGS().maps("屋台", country="Japan", city="Fukuoka", max_results=3)

        print(results)
        """
    )

with tab2:
    if st.button("Search"):
        results = DDGS().maps("屋台", country="Japan", city="Fukuoka", max_results=3)
        st.write(results)
