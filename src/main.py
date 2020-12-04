from bookmark import Bookmark
import MeCab
import os
from wordcloud import WordCloud

#ワードクラウドの作成
def create_wordcloud(titles):
    fontpath = '/work/.fonts/' + os.environ['FONTFILE']
    stop_words = ['Qiita', 'note', 'Speaker Deck', 'まとめ', 'コリス', 'blog']

    tagger = MeCab.Tagger(
        '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
    )
    tagger.parse('')
    word_list = []
    for title in titles:
        node = tagger.parseToNode(title)

        while node:
            word_type = node.feature.split(',')[0]
            word_surf = node.surface.split(',')[0]
            if word_type == '名詞':
                if (node.surface not in stop_words) and \
                    len(set(["副詞可能", "数", "非自立", "代名詞", "接尾"]) \
                        & set(node.feature.split(",")[1:4])) == 0:
                    word_list.append(node.surface)
            node = node.next

    word_chain = ' '.join(word_list)
    wordcloud = WordCloud(background_color=None,
                          mode="RGBA",
                          font_path=fontpath,
                          width=900,
                          height=500,
                          relative_scaling=0.5 # フォントサイズの相対的な単語頻度の重要性
                         ).generate(word_chain)

    #ファイルの作成
    wordcloud.to_file("/work/images/image-" + os.environ['HATENAID'] + ".png")

def main():
    hatena_id = os.environ['HATENAID']
    bookmark = Bookmark(hatena_id)
    titles = bookmark.get_title()

    create_wordcloud(titles)

if __name__ == "__main__":
    main()
