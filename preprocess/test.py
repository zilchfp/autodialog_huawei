#-*- encoding:UTF-8 -*-

posts_file=open('../db/post.txt',mode='r',encoding='UTF-8')

posts=posts_file.readlines()

with open('../db/post_test.txt',mode='w',encoding='UTF-8') as f:
    for i in range(1000):
        f.write(posts[i])
