# DuckDuckGoデモアプリ
DuckDuckGoを試せるデモアプリ by Streamlit

## 準備
### Dockerイメージ作成
```
docker image build -t duckduckgo .
```

## 実行方法
```
docker container run --rm -it -v $(pwd):/app -p 8501:8501 duckduckgo bash
streamlit run home.py
```

以下にアクセス。

http://localhost:8501/

## 終了方法
- Ctrl + cでStreamlit終了。
- "exit"と入力すればコンテナ終了・削除