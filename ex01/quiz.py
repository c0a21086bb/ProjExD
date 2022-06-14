#未完成
def main():
    seikai = shutudai()
    kaitou(seikai)


def shutudai():
    qas = ["サザエの旦那の名前は?", 
                "カツオの妹の名前は?",
                "タラオはカツオから見てどんな関係?"]
    answer = [["マスオ", "ますお"],
              ["ワカメ", "わかめ"],
              ["甥", "おい", "甥っ子", "おいっこ"]]
    import random
    question_number = (randint(0,2))
    print(question(question_number))


def kaito():
    player_answer = input("答えるんだ : ")
    if player_answer == answer[question_number]:
        print("正解！！！")
    else:
        print("出直してこい")


if __name__ == "__main__":
    main()