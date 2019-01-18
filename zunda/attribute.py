from . import zunda
from . import zunda_sub

text="a.txt" #ここに解析対象文を入れる

def main(txt):
    zunda_sub.main(txt)
    zunda_txt="zunda_out.txt"
    words=zunda.main(zunda_txt)
    return zunda.zokusei_out(words)

if __name__ =="__main__":
    main()
