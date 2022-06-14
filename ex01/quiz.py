import random
import datetime

def main():
    st = datetime.datetime.now()
    seikai = shutudai()
    kaitou(seikai)
    ed = datetime.datetime.now()
    print("回答時間"+str(((ed-st).seconds))+"秒")

def shutudai():
    qas = [
           {"q": "サザエの旦那の名前は？", "a": ["マスオ", "ますお"]},
           {"q": "カツオの妹の名前は？", "a": ["ワカメ", "わかめ"]},
           {"q": "タラオはカツオから見てどんな関係？", "a": ["甥", "おい", "甥っ子", "おいっこ"]},
           ]
    print("問題 : ")
    r = random.randint(0,2)
    print(qas[r]["q"])
    return qas[r]["a"]

def kaitou(seikai):
    ans = input("答えるんだ : ")
    if ans in seikai:
        print("正解！！！")
    if ans == "33-4":
        print("何でや！阪神関係ないやろ！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()