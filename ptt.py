try:
    score = int(input("分数:"))
    Difficulty = float(input("谱面定数:"))
except ValueError:
    print("格式错误")
else:
    if score >= 10000000:
        ptt = Difficulty + 2
        print("您的单曲ptt是:%.2f" % ptt)
  # elif score >= 9800000 and score < 100000000:
    elif 9800000 <= score < 100000000:
        ptt = Difficulty + 1 +(score-9800000)/200000
        print("您的单曲ptt是:%.2f" % ptt)
    elif score < 9800000:
        ptt = Difficulty + (score-950000)/300000
        print("您的单曲ptt是:%.2f" % ptt)
