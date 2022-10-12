import spacy

def check_en_doc_similarity(answer_list,key_list):
    nlp = spacy.load('en_core_web_lg')
    similarity_list = []
    
    for i in range(len(answer_list)):
        similarity = round(nlp(answer_list[i]).similarity(nlp(key_list[i])),2)
        if similarity > 0.7:
            similarity_list.append(1)
        else:
            similarity_list.append(0)
            
    grade = similarity_list.count(1)/len(similarity_list)
    print(grade*100)
    return grade*100

check_en_doc_similarity(["A","b","b","ASD"],["A","b","b","ASD"])