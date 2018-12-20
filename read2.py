data = []
count = 0
with open('reviews.txt', 'r') as t:
    for line in t:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取結束，總共有', len(data), '筆資料')

# 計算留言平均長度
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
    print(sum_len)
print('留言的平均長度是', sum_len/len(data))
print('----------------------------')
print('')

# 只讀出資料中的第一筆留言與第二筆留言
print(data[0])
print('----------------------------')
print('')
print(data[1])