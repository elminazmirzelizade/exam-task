from operator import index
from os import sep


questions = [
    {
        'question': 'Asagidakilardan hansi bitkiler alemine aiddir?',
        'options': ['Ordek', 'Gobelek', 'At', 'Sam agaci'],
        'answer': 3
    },
    {
        'question': 'Bunlardan hansi saitdir?',
        'options': ['b', 'a', 'c', 'd'],
        'answer': 3
    },
    {
        'question': 'En boyuk materik hansidir?',
        'options': ['Antarktika', 'Avstraliya', 'Avrasiya', 'Simali Amerika'],
        'answer': 2
    },
    {
        'question': 'Azerbaycan Respublikasi ne vaxt yaranib?',
        'options': ['1928', '1918', '1500', '1930'],
        'answer': 1
    },
    {
        'question': 'Quvvetin vahidi?',
        'options': ['Newton', 'Vold', 'Watt', 'Metr'],
        'answer': 0
    },
    {
        'question': 'Asagidakilardan hansi radioaktivdir?',
        'options': ['Plutonium', 'Cive', 'Lithium', 'Cupper'],
        'answer': 0
    },
    {
        'question': 'Bextiyar Vahabzedenin ilk seiri hansidir?',
        'options': ['Leyli ve Mecnun', 'Latin dili', 'Ana ve Sekil', '20 yanvar'],
        'answer': 2
    },
    {
        'question': 'sin90 nece edir?',
        'options': ['1', '2', '3', '4'],
        'answer': 0
    },
]

eq = {'a': 0, 'b': 1, 'c': 2, 'd': 3}



"""
1. sin90 nece edir?
A) 1
B) 2
C) 3
D) 4

Cavabi girin: 


1. sin90 nece edir?
A) 1
B) 2
C) 3
D) 4

Cavabi girin: 
------------------------
Sizin neticeni 8 uzerinden 7

"""
question_number = 0
true_answer=0
for exam_full_question in questions:
    print(question_number,'. ',exam_full_question['question'], sep='')
    question_number = question_number + 1
    print('A: ',exam_full_question['options'][0])
    print('B: ',exam_full_question['options'][1])
    print('C: ',exam_full_question['options'][2])
    print('D: ',exam_full_question['options'][3]) 
    print('')
    telebenin_cavabi=input('Cavabi girin: ').lower()
    # print(telebenin_cavabi)
    # print(list(eq).index(telebenin_cavabi)) 
    # print(exam_full_question['answer'])
    # print(list(eq)[exam_full_question['answer']])
    
    if(list(eq).index(telebenin_cavabi)==exam_full_question['answer']):
        print('Dogru cavabdir')
        true_answer=true_answer+1 
    else:
        print('Yanlis cavabdir. Dogru cavab',list(eq)[exam_full_question['answer']].upper(),'variantidir')
print('--------------------------')
print('Sizin neticeniz', len(questions),'uzerinden',true_answer,'dir')


    





    



   

            