#-*- encoding:UTF-8 -*-
from pyltp import Postagger
"""实现对post和resp文件（包括ltp分词和原始分词）的词性标注，按照nltk语料的格式（但是由于中文编码
   不能被nltk的部分函数支持）"""


"""初始化实例并加载模型"""
postagger = Postagger()
postagger.load(r'C:\workresource\AI\nlp\ltp_data\pos.model')

post_file=open(r"C:\workspace\python\project\autodialog\db\post.txt",mode="r",encoding='UTF-8')
resp_file=open(r"C:\workspace\python\project\autodialog\db\resp.txt",mode="r",encoding="UTF-8")
posts=post_file.readlines()
resps=resp_file.readlines()

with open(r"C:\workspace\python\project\autodialog\db\post_tag_nltk.txt","w",encoding="UTF-8") as f:
    for line in posts:
        words=line.strip().split(' ')
        postags=postagger.postag(words)
        sents =[]
        for i in range(len(words)):
            sents.append(words[i]+'/'+postags[i])
        f.write(' '.join(sents)+'./.'+'\t') #./.的作用是便于nltk分句的识别，下同

with open(r"C:\workspace\python\project\autodialog\db\resp_tag_nltk.txt","w",encoding="UTF-8") as f:
    for line in resps:
        words=line.strip().split(' ')
        postags=postagger.postag(words)
        sents =[]
        for i in range(len(words)):
            sents.append(words[i]+'/'+postags[i])
        f.write(' '.join(sents)+'./.'+'\t')

post_orig_cut=open(r"C:\workspace\python\project\autodialog\db\post_orig_cut.txt",mode="r",encoding='UTF-8')
resp_orig_cut=open(r"C:\workspace\python\project\autodialog\db\resp_orig_cut.txt",mode="r",encoding="UTF-8")
posts_orig=post_orig_cut.readlines()
resps_orig=resp_orig_cut.readlines()

with open(r"C:\workspace\python\project\autodialog\db\post_tag_nltk_orig_cut.txt","w",encoding="UTF-8") as f:
    for line in posts_orig:
        words=line.strip().split(' ')
        postags=postagger.postag(words)
        sents =[]
        for i in range(len(postags)):
            sents.append(words[i]+'/'+postags[i])
        f.write(' '.join(sents)+'./.'+'\t')

with open(r"C:\workspace\python\project\autodialog\db\resp_tag_nltk_orig_cut.txt","w",encoding="UTF-8") as f:
    for line in resps_orig:
        words=line.strip().split(' ')
        postags=postagger.postag(words)
        sents =[]
        for i in range(len(postags)):
            sents.append(words[i]+'/'+postags[i])
        f.write(' '.join(sents)+'./.'+'\t')
