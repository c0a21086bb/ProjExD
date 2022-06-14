import random
import datetime

kaisuu = 10   #試行可能回数
kesson = 3    #欠損文字数
taisyou = 10  #対象文字数

def main():
    st = datetime.datetime.now()
    for i in range(kaisuu):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
    ed = datetime.datetime.now()
    print(f"回答時間 : {str((ed-st).seconds)}秒")


def shutudai():
    all_alphabet = [chr(c+65) for c in range(26)]        #AからZまでのアルファベットのリストを作成
    alphabets = random.sample(all_alphabet, taisyou)     #アルファベットを対象の文字数分選ぶ
    print(f"対象文字: {alphabets}")

    kesu = random.sample(alphabets, kesson)     #文字を消す
    #print(f"欠損文字: {kesu}")     #消えた文字の表示(デバッグ用)

    mondaibun = [c for c in alphabets if c not in kesu]    #文字が消えた後のリストを作成
    print(f"表示文字{mondaibun}")

    return kesu

def kaitou(seikai):
    kietakazu = int(input("欠損文字はいくつあるでしょうか? : "))
    if kietakazu != kesson:
        print("不正解です。またチャレンジしてください。")
        print("-"*50)
        return 0
    else:
        print("正解です。それでは具体的に欠損文字を1文字づつ入力してください。")
        for i in range(kesson):
            c = input(f"{i+1}番目の文字を入力してください。")
            if c not in seikai:
                print("不正解です。またチャレンジしてください。")
                print("-"*50)
                return 0
            seikai.remove(c)
        print("正解です。ゲームを終了します。")
        return 1
        

if __name__ == "__main__":
    main()