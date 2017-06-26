songn=[]
#add the song name
while(1):
    newsong=raw_input('Enter the name of song(if end,enter -1):')
    if(newsong=='-1'):
        break
    else:
        songn.append(newsong)
#only keep 5 songs
while(len(songn)>5):
    songn.pop()
print 'the 5 most popular song are:'
print songn
    
