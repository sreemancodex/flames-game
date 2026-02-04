first_name=input("enter the name 1:")
second_name=input("enter the name 2:")
first_name_list=list(first_name.lower())
second_name_list=list(second_name.lower())
print(first_name_list)
print(second_name_list)
for s in first_name_list:
    if s in second_name_list:
        print("similar letter in both names:",s)
        k=first_name_list.index(s)
        first_name_list[k]='*'
        k=second_name_list.index(s)
        second_name_list[k]='*'
print(first_name_list)
print(second_name_list)
count=0
combine_names=first_name_list+second_name_list
for s in combine_names:
    if(s!="*" and s!=" "):
        count+=1
print(count)   
index=0
f=list('FLAMES')
print(f)
while len(f)>1:
    for i in range(count):
        index+=1
        if(index>len(f)):
            index=1
    f.remove(f[index-1])
    index-=1
#print(f)
if(f==['F']):
    print("FRIEND")
    print(first_name,second_name,"are the Bestestestest friend in the whole world!!!!")
elif(f==['L']):
    print("LOVE")
    print(first_name,"LOVE",second_name,"unconditionally even after their death.....")        
elif(f==['A']):
    print("AFFECTION")  
    print(first_name,"and",second_name,"affectionate and love each other infinitely till the die....")
elif(f==['M']):
    print("MARRIAGE")
    print(first_name,"succeded in his life and married",second_name,".They both lived a beautiful life ")    
elif(f==['E']):
    print("ENEMY")
    print(first_name,second_name,"They have  a enemy relationship!!!") 
elif(f==['S']):
    print("SIBLING")
    print(first_name,second_name,"are kindest and favourite the sibling in their life")
else:
    print("sorry.",first_name,"did not have any relationship with ",second_name)                
        