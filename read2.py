data = []
count = 0
with open('reviews.txt', 'r') as t: # 這一行是將reviews.txt資料讀進來程式中的前置作業
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

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '筆提到 "good"')

# 同line34~37的快寫法 (學起來可以精簡流程）
good = [d for d in data if 'good' in d] # 此為一個list
print('一共有', len(good), '筆提到 "good"')

good = [1 for d in data if 'good' in d]
print(good)

# 下方line48為一句布林句子
bad = ['bad' in d for d in data]
print(bad)
# 等於line47
# bad = []
# for d in data:
#     bad.append('bad' in d)


# 列印出留言中有出現 bad or worse的留言
argue = [d for d in data if 'bad' or 'worse' in d]
print(argue)