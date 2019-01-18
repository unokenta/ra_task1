import re
from . import subproses

a_stop = ["自分","私","僕","俺","私達"] #Bが主体(id)のフィルタ
b_stop = ["いる","ある","なる","する"] 
c_stop = ["あれ","それ","これ","そこ"] #代名詞の区別(「彼」「彼女」などと)

def get_subject(text):
    with open(text) as data_file:
        ids=[]
        subject=[]
        sentense=[]
        sentenses=[]
        ga=[]
        sub_frag=0
        for line in data_file:
            tab=line.split('\t')
            if "EOS" in tab[0]:
                
                #文末に主体判定([主体がある文か]and[自分か自分以外])
                frag=out(subject,ga)

                #一文を出力
                #print(str("".join(sentense)))
                
                #場合分けして出力(frag=1:主体は自分(B) , frag=0:自分以外 , none:主体なし)
                if frag == 1:
                    #print("subject is B")
                    return "B" 
                elif frag==0:
                    #print("subject is not B")
                    return "other"
                else:
                    #print("none")
                    return None
                
                #複数分の場合リスト化
                sentense_dic={
                    "sentense":str("".join(sentense)),
                    "frag":frag,
                    }
                sentenses.append(sentense_dic)
                
                sentense=[]
                subject=[]
                ga=[]
                
            if len(tab)>2:
                sentense.append(tab[0])
                verb=tab[1].split(',')

                #id(主体)が存在すれば情報取得
                if 'id' in tab[3]:
                    id_number=re.search(r"id=\"(\d+)\"",tab[3])
                    id_dic={
                        'main':tab[0],
                        'id_number':id_number.group(1),
                        'noun':verb[0],
                        '2':verb[1],
                        '3':verb[2]
                    }
                    subject.append(id_dic)

                #ga格の情報取得
                if 'ga' in tab[3]:
                    ga_number=re.search(r"ga=\"(\d+)\"",tab[3])
                    ga_dic={
                        'main':tab[0],
                        'base':verb[6],
                        'ga_number':ga_number.group(1),
                        'noun':verb[0],
                        '2':verb[1],
                        '3':verb[2],
                        'katuyou':verb[5],
                        'flag':0
                    }
                    ga.append(ga_dic)
                    sub_frag=1
                    
        #主体とガ格のリストを返す
        #return subject,ga

def out(subject,ga):
    for a in subject:
        for b in ga:
            #以下の条件を満たすとき主体はB(自分)
            if a['id_number']==b['ga_number'] and not '名詞' in b.values() and not '形容詞' in b.values():
                
                if ('非自立' in a.values() and '自立' in b.values()) :
                    b['flag'] = 1      # flag=1→主体はB
                for s1 in a_stop :
                    if s1 in b.values() or s1 in a.values():
                        b['flag'] = 1                       

                for s2 in c_stop :
                    if s2 in a.values():
                        b['flag'] = 1
                        
                if b['flag'] == 1:
                    #print("subject is B")
                    #print("B",a['id_number']+"\t"+a['main']+" が "+b['base'])
                    return b["flag"]
                else :
                    #print("subject is not B")
                    #print("*",a['id_number']+"\t"+a['main']+" が "+b['base'])      
                    return b["flag"]

def main(txt):

    subproses.main(txt)
    syncha_text="syncha_out.txt"
    return get_subject(syncha_text)
    #out(subject,ga)

"""                    
if __name__=="__main__":
    
    txt="a.txt" #解析対象文

    main(txt)
"""

    
"""
表示形式[主体][id][主体原型][属性][述語原型][属性]                        
                if b['flag'] == 1:
                    print("B",a['id_number']+"\t"+a['main']+"\t"+a['noun']+" "+a['2']+" "+a['3']+"\tBが"+b['base']+"\t"+b['noun']+" "+b['2']+" "+b['3']+" "+b['katuyou'])                           
                else :
                    print("*",a['id_number']+"\t"+a['main']+"\t"+a['noun']+" "+a['2']+" "+a['3']+"\t*が"+b['base']+"\t"+b['noun']+" "+b['2']+" "+b['3']+" "+b['katuyou'])      
"""                                               
                            




