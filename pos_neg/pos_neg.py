import MeCab

pos_list=["はい","そう","ええ","そうですね","です"]
neg_list=["いいえ","いや","いやいや","ない","違い"]


def main(text):

    m = MeCab.Tagger("-Owakati")
    
    meta=m.parse(text).split(" ")
    
    for neg in neg_list:
        #文頭または文末に否定文
        if neg == meta[0] or neg == meta[-2] or neg == meta[-3] or neg == [-4]:
            #print("this is negative response")
            return "negative"

    for pos in pos_list:
        if pos == meta[0]:
            #print("this is positive response")
            return "positive"

    #print("this is neutral")
    return "neutral"

    
if __name__ == "__main__":

    with open(txt) as f:
        flag=0
        for line in f:
            if "A" in line:
                flag=0
                print(line.replace("\n",""))
            elif flag == 1:
                print(line.replace("\n",""))
                continue
            else:
                flag=1
                sub=line.replace("A:","").replace("B:","")
                print(line.replace("\n",""))
                pos_neg(sub)
            
