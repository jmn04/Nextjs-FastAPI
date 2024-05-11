# U22_ATRI
U22プログラミングコンテストに向けて作成したアプリのリポジトリです。
Next.jsのApp Routerを使うことになったため、このリポジトリは使いません。
(最終更新：2024/05/11)

<br>

# 利用技術
- フロントエンド：Next.js（React, TypeScript）
- サーバーサイド：FastAPI, OpenCV, MediaPipe（Python）
- データベース：PostgreSQL（SQLAlchemy）

<br>

# Dockerのセットアップ
- Docker Desktopがインストール出来ていない　－＞　1番参照
- それ以外　－＞　2番参照
<br>

### 1. Docker Desktopのインストール
- dockerを用いたコンテナ開発を行うにあたり、Docker Desktopのインストールが必要です。
- [こちら](https://www.docker.com/ja-jp/products/docker-desktop/)からダウンロードしてください。

<br>

### 2. コンテナを構築する
- はじめに、Docker Desktopを起動してください。
- コマンドプロンプトを立ち上げ、`git clone https://github.com/jmn04/U22_ATRI.git`を実行し、`U22-ATRI`リポジトリをローカルにクローンしてください。
- `cd U22-ATRI`でU22-ATRIがカレントディレクトリになるようにします。
- コマンドプロンプトにて`docker-compose build`を実行してdockerイメージをビルドします。
![docker-compose build](images/docker-compose_build_image.png)
![Docker Desktop build](images/docker-desktop_build_image.png)
- 続いて`docker-compose up`を実行してコンテナを作成・実行します。
- ネットワーク通信の許可を要求された場合、**許可**してください。
  許可しなければ正常に動作しません。
![docker-compose up](images/docker-compose_up_image.png)
![Docker Desktop up](images/docker-desktop_up_image.png)

- 実行中のコンテナを停止するには、`Ctrl + C`キーで停止してください。
![docker stopped](images/docker_stopped_image.png)
![Docker Desktop stopped](images/docker-desktop_stopped_image.png)

<br>

### 3. コンテナとイメージを削除する
- コマンドプロンプトにて`docker-compose down`を実行してコンテナを停止・削除します。
- 続いて、`docker images`を実行し、作成されたイメージを確認します。「u22_atri-*」となっているものが今回作成されたイメージです。。
-   `docker rmi {IMAGE-ID}`を実行してください。この際、中かっこは不要です。`docker rmi {IMAGE-ID IMAGE-ID}`のように複数削除することもできます。
- `docker-compose build`によって同じものを再度作成できるので消しても特に問題ありません。
