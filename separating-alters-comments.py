
# coding: utf-8

# In[51]:

def separate_name_message():
    file=open("E:/saddam-to-others.txt","r")
    lines=file.readlines()
    file.close()

    name='\"name\":'
    msg='\"message\":'
    frnd_names=[]
    frnd_comments=[]
    for f in lines:
        l=f.strip()
        if name in l:
            #print l[9:-2]
            frnd_names.append(l[9:-2])
        
        if msg in l:
            #print l[12:-2]
            frnd_comments.append(l[12:-2])

    if len(frnd_names)==len(frnd_comments):
        return frnd_names,frnd_comments # Returning two list together
        #userfrequency = {i:frnd_names.count(i) for i in frnd_names}
    
#print userfrequency

def comments_writing_to_files():
    ego="saddam" #put ego name here
    fnames, fcomments = separate_name_message() #Receiving two lists together
    userfrequency = {i:fnames.count(i) for i in fnames}
    for key,val in userfrequency.items():
        #print "Key",key
        #print "Val",val
        if val==1:
            indx=0
            for k in fnames:
                indx=indx+1
                if key==k:
                    try:
                        file = open("E:/ego/"+key+"-"+ego+"_.txt","w") 
                        #print key
                        #print indx
                        #print frnd_comments[indx-1]
                        file.write(frnd_comments[indx-1])
                        file.close()
                    except:
                        continue
                        
        if val>1:
            txt=''
            idx=0
            for n in fnames:
                idx=idx+1
                if key==n:
                    txt=txt+frnd_comments[idx-1]+"\n"
            file = open("E:/ego/"+key+"-"+ego+"_.txt","w")
            file.write(txt)
            file.close()
            txt=''       
            
        
if __name__ == '__main__':
    comments_writing_to_files()#Separate comments by reading from a csv file


# In[ ]:



