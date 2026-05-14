# coding: shift_jis
while True:
    Input=input("0~9の数字を,で区切って複数入力してください")
    print("Input > ",Input)
    Input = Input.replace(" ", "") #空白を消している
    if not Input.strip():
        print("数字を入力してください")
        continue
    
    
    # 1~9 の数字以外が含まれているか判定
    int_Input = any(x not in "0123456789," for x in Input)
    if int_Input:
        print("1~9以外の値が含まれています")
    elif not Input:
        print("数字を入力してください")
    else:
        break
    
Input = Input.split(",")       #,で文字を区切る
n = len(Input)                 #リストの個数をnとする
    
Input = [int(s) for s in Input]
Input = sorted(Input) #順番通りに並び替える
print("Output > ",Input)