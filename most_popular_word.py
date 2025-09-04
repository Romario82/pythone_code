reviews = [
    "Очень хороший телефон, но батарея быстро садится",
    "Телефон отличный, камера супер!",
    "Ноутбук мощный, экран большой",
    "Камера у телефона плохая, не советую",
    "Отличный ноутбук за свои деньги",
    "Телефон нормальный, но камера могла быть лучше"
]
    
    
def most_popular_word(reviews):
    stop_words = {
        "и", "но", "а", "у", "за", "с", "на", "о", "от", "под", "над", "в",
        "во", "же", "то", "это", "эти", "этот", "эта", "того", "той", "те",
        "свои", "своё", "своя", "их", "его", "ее", "её", "бы", "же", "ли",
        "как", "так", "для", "что", "чтобы", "все", "всё"
    }
    
    data_d = {}
    
    for review in reviews:
        words = review.lower().split()
        print(words)
        for word in words:
            word = word.strip(".,!?")
            if word not in stop_words:
                data_d[word] = data_d.get(word, 0) + 1
            print (data_d)
            
    return max(data_d.items(), key=lambda x: x[1])
    
print(most_popular_word(reviews))  
# -> ("телефон", 3)
    
print(most_popular_word(reviews))  
