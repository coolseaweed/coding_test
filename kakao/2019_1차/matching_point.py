import numpy as np
import re

def search_prase_index(word_list, word):


    start_word = '<'+word+'>'
    end_word = '</'+word+'>'

    for index, x in enumerate(word_list):
        if x == start_word :
            start_index = index

        if x == end_word:
            end_index = index

    return start_index, end_index

def search_url(word_list, where):

    start, end = search_prase_index(word_list,where)
    
    url_list =[]

    for index in range(start+1, end):
        temp = word_list[index].split('"')
        for x in temp:
            if x.find("https") != -1:
                url_list.append(x)



    return url_list


def find_word_cnt(word_list,word):


    start, end = search_prase_index(word_list,'body')
    cnt = 0

    p = re.compile('[a-zA-Z]+')


    for index in range(start+1, end):

        #temp = word_list[index].split(" ")
        temp = p.findall(word_list[index])
        #print(temp)
        for x in temp:
            if x.lower() == word:
                cnt +=1
        #print(" - - - - - - - - - - - ")

    return cnt





def solution(word, pages):

    history = []
    for page in pages:

        temp = page.split('\n')
        word_list = [x.strip() for x in temp]
        basic_point = find_word_cnt(word_list,word)
    
        my_url = search_url(word_list,'head')[0]
        linked_url = search_url(word_list,'body')
        history.append({'my_url':my_url, 'linked_url':linked_url, 'basic_point':basic_point})


    point_values = []
    for x in history:
        url = x['my_url']
        cnt = x['basic_point']

        for y in history:
            if y['my_url'] == url:
                continue
            else:
                for z in y['linked_url']:
                    if url == z:
                        cnt += y['basic_point']/len(y['linked_url'])
        
        print(url, cnt ,'\n')
        point_values.append(cnt)
    
    answer = np.argmax(point_values)


    return answer






pages = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem BLIND ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", 
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"
    ]

word = 'suspendisse'

answer = solution(word,pages)

print(answer)