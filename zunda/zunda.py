def main(data):
    with open(data) as text:
        words=[]
        word=[]
        event_list=[]
        word_number=0
        future_number=-1
        future_frag=0
        for line in text:
            elements=line.split("\t")
            if "#" in elements[0] :
                if "EVENT" in elements[0]:
                    time=elements[3]
                    event_list.append(elements[5])
                    if time=="未来" :
                        future_number=elements[1]
                continue

            if "EOS" in elements[0]:            
                words.append(word)
                word=[]
                event_list=[]
                word_number=0
                future_frag=0
                future_number=-1
                continue

            if len(elements)==2:
                types=elements[1].split(",")
                word_dic={
                    "word":elements[0],
                    "type1":types[0],
                    "type2":types[1],
                    "past_frag":0,
                    "future_frag":0,
                    "word_number":word_number,
                    "event_list":event_list
                }
            
                word_number+=1
                word.append(word_dic)
                
            #未来判定
            try:
                if int(word_number) == int(future_number):
                    future_frag=1
                    
                if future_frag==int(1) and word_dic["type1"]=="動詞":
                    word_dic["future_frag"]=1
                    future_frag=0
            except:
                future_frag=0
                continue
            
        #過去判定
        for fact in words:
            past_frag=0
            for i,s in enumerate(fact):
                if past_frag==1 and s["word"]=="た" :
                    #s["past_frag"]=1
                    fact[i-1]["past_frag"]=1 
                if s["type1"] == "動詞": #「動詞+た」
                    past_frag=1
                if s["word"] == "まし" and s["type1"]=="助動詞":
                    past_frag=1
                else:
                    past_frag=0
    return words 

def zisei_out(words):
    for outs in words:
        print("")
        tense_frag=0
        for out in outs:
            #print(out["word"],end="")
            
            if out["past_frag"]==1:
                #print("[過去]",end="")
                tense_frag=1
                continue

            if out["future_frag"]==1:
                #print("[未来]",end="")
                tense_frag=2
                continue

            if out["type1"]=="動詞" :
                if not (out["future_frag"]==1 and out["past_frag"]==1) :
                    tense_frag=0
                    #print("[現在]",end="")

        if tense_frag==0:
            #print("this sentense is present")
            return("present")
        elif tense_frag==1:
            #print("this sentense is past")
            return("past")
        elif tense_frag==2:
            #print("this sentense is future")
            return("future")
            
def zokusei_out(words):
    for outs in words:
        event_frag=0
        
        for out in outs:
            #print(out["word"],end="") #文出力
            if out["event_list"] :
                event_frag=1
                
        if event_frag==1:
            #print("\n event is" , list(set(out["event_list"])))
            return list(set(out["event_list"]))
        else:
            #print("\n no event")
            return None
            
if __name__=="__main__":
    words=main(data)
    zokusei_out(words)
