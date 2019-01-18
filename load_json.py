import json
import subprocess

from syncha import subject 
from syncha import subproses

from zunda import attribute
from zunda import zunda_sub
from zunda import tense

from pos_neg import pos_neg

from emotion import emotion


def take_sentense(json_file):
    with open(json_file) as f:        
        df_list=json.load(f)
        frag=0
        for i,df in enumerate(df_list["utterances"]):

            print("sentense is",df["utterance"])
            
            df["subject"]=subject.main(df["utterance"])            
            df["dialog_act"]=attribute.main(df["utterance"])
            df["tense"]=tense.main()
            df["emotion"] = emotion.main2(df["utterance"])
            
            if df["speaker"]=="B" and df_list["utterances"][i-1]["speaker"]=="A":
                df["response"]=pos_neg.main(df["utterance"])
            else:
                df["response"]=None
        return df_list
        
        
if __name__=="__main__":
    file_name="data/S01T01.json"
    d=take_sentense(file_name)
    with open('new.json', 'w') as f:
        json.dump(d, f,ensure_ascii=False,indent=3)
            
