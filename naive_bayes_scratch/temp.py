import re

text = u'Vô cái quán bất ngờ đủ thứ :))Bảng giá 1 tô 2 tô .. 10 tô , ban đầu mình tưởng ăn càng nhìu tô giá càng bớt, ai ngờ, chỉ là để vậy cho rõ ràng, tính giá cho nhanhTô 3 miếng cật mà miếng nấy to đùng luôn :)) thịt băm và hẹ cũg ngất ngưỡng. Tô 42k nhaTrên bàn ko có ji ngoài 2 chai xi dầu nc mắn và tăm, còn lại trà đá 4k,khăn ướt, ot sa tế khách đến mới mang ra :))@ni_cherry'
text = re.sub('[^\w\s]+', '', text, flags=re.IGNORECASE)
if re.match(r'\w', text):
    text = re.sub(
        '[-@_!#$%^&*()<>?/\|}{~:]', ' ', text, flags=re.IGNORECASE)
else:
    text = ''

text = re.sub(r"[^\w\s]+", "", text, flags=re.UNICODE)
print(text)
