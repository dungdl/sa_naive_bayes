from pyvi import ViTokenizer, ViPosTagger
import nltk

sen = u"_ Ảnh chụp từ hôm qua, đi chơi với gia đình và 1 nhà họ hàng đang sống tại Sài Gòn. _ Hôm qua đi ăn trưa muộn, ai cũng đói hết nên lúc có đồ ăn là nhào vô ăn liền, bởi vậy mới quên chụp các phần gọi thêm với nước mắm, chỉ chụp món chính thôi! _ Đói quá nên không biết đánh giá đồ ăn kiểu gì luôn 😅😅😅_ Chọn cái này vì thấy nó lạ với tui."
tokens = ViTokenizer.tokenize(sen)

tokens = nltk.word_tokenize(tokens)
print(tokens)
