# -*- coding: utf-8 -*-
#韩红歌曲列表
#listhh=['天路','天亮了','青春','那片海','美丽的神话','谈何容易']
listhh=['天路\n','天亮了\n','青春\n','那片海\n','美丽的神话\n','谈何容易\n']
listfile=open('listfile.txt','w')
listfile.writelines(listhh)
listfile.close()

