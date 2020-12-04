# myword-cloud

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
