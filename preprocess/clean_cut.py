#-*- encoding:UTF-8 -*-
from pyltp import Segmentor
import sys

"""对原始语料的清理和分词，实现包括去除特殊字符、与问答不相关字段、纯英文或其他非中文字符问答等
   并根据分词的依据，将post和resp生成post.txt/post_orig_cut.txt和resp.txt/resp_orig_cut.txt"""

"""初始化实例并加载模型"""
segmentor=Segmentor()
segmentor.load(r'C:\workresource\AI\nlp\ltp_data\cws.model')

post_file=open(r"C:\workspace\python\project\autodialog\stc_weibo_train_post",mode="r",encoding='UTF-8')
resp_file=open(r"C:\workspace\python\project\autodialog\stc_weibo_train_response",mode="r",encoding="UTF-8")
posts=post_file.readlines()
resps=resp_file.readlines()

"""本部分被注释代码是重新分词的实现代码，注释部分下面部分的对应代码代表用的原来分词结果"""
# with open(r"C:\workspace\python\project\autodialog\db\post.txt","w",encoding="UTF-8") as f_post:
with open(r"C:\workspace\python\project\autodialog\db\post_orig_cut.txt","w",encoding="UTF-8") as f_post:
    # with open(r"C:\workspace\python\project\autodialog\db\\resp.txt", "w", encoding="UTF-8") as f_resp:
    with open(r"C:\workspace\python\project\autodialog\db\\resp_orig_cut.txt", "w", encoding="UTF-8") as f_resp:
        for i in range(len(posts)):
            # sent_post=''
            # sent_resp=''
            sent_post=[]
            sent_resp=[]

            chn_post_flag=0
            post=posts[i].split(' ')
            if len(post)>=2 and post[-1].strip() in [')','）','\u300D']:#对于发布的微博结束部分的'（）'一般都是与来源和版权声明，与语义无关
                while len(post)>=2 and post[-1].strip() not in ['(','（','\u300C']:
                    post.pop()
                post.pop()
            for word in post:
                word=word.strip() #去除首尾空格
                if word>='\u4e00' and word<='\u9fa5': #保证包含中文，纯英文或者其他字符的句子不要
                    chn_post_flag=1
                if len(word)!=0 and sys.getsizeof(word[0])==80: continue #剔除特殊字符
                if word in ['【', '#', '#','alink']: continue  # 剔除无用字符
                # if word<='z' and word>='a':
                #     word=' '+word
                if word in ['】']:word=','
                # sent_post=sent_post+word
                sent_post.append(word)

            chn_resp_flag=0
            resp=resps[i].split(' ')
            for word in resp:
                word=word.strip() #去除首尾空格
                if word >= '\u4e00' and word <= '\u9fa5':# 保证包含中文，纯英文或者其他字符的句子不要
                    chn_resp_flag = 1
                if len(word)!=0 and sys.getsizeof(word[0])==80: continue #剔除特殊字符
                if word in ['【', '#','#', 'alink']: continue  # 剔除无用字符
                # if word <= 'z' and word >= 'a':
                #     word = ' ' + word
                if word in ['】']: word =','
                # sent_resp=sent_resp+word
                sent_resp.append(word)

            if chn_post_flag and chn_resp_flag:
                # words_post=segmentor.segment(sent_post)
                # words_resp=segmentor.segment(sent_resp)
                # f_post.write(' '.join(words_post)+'\n')
                # f_resp.write(' '.join(words_resp)+'\n')
                f_post.write(' '.join(sent_post)+'\n')
                f_resp.write(' '.join(sent_resp)+'\n')


post_file.close()
resp_file.close()
