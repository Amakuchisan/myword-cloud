# myword-cloud

あるユーザの、はてなブックマークした記事のタイトルを取得して、ワードクラウドの画像を生成します。
https://cnaan.hatenablog.com/entry/2020/12/04/234523

## 事前に用意するもの

- 日本語のフォントファイル
  - .fontsディレクトリにコピー

## 実行

${はてなID}には、ワードクラウドを作成したいユーザのはてなIDを入れて実行します。

```
$ git clone https://github.com/Amakuchisan/myword-cloud.git
$ cd myword-cloud
$ docker build -t myword-cloud:1.0 .
$ docker run -it --rm --name myword-cloud -e HATENAID=${はてなID} -v $(pwd)/images:/work/images myword-cloud:1.0
```

## はてなID

Dockerfileで、デフォルトのHATENAIDを、sampleにしています。
http://developer.hatena.ne.jp/ja/documents/bookmark/misc/feed

## ユーザ辞書について

userdic/myDic.csvに、追加したい単語を記述します。
```
表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音(,その他あれば自由に追加)
```
