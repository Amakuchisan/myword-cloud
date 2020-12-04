FROM python:3.9.0

WORKDIR /work
COPY requirements.txt requirements.txt

RUN pip install -U pip \
    && pip install -r requirements.txt
# RUN pip install -U pip\
#     && pip install fastprogress japanize-matplotlib

# mecabとmecab-ipadic-NEologdの導入
RUN apt-get update \
    && apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file sudo

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && bin/install-mecab-ipadic-neologd -n -y \
    && ln -s /etc/mecabrc /usr/local/etc/mecabrc

# 環境変数にはてなIDをセット
ENV HATENAID CNaan
COPY . .

CMD ["python", "bookmark.py"]
