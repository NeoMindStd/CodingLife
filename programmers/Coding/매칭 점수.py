import re

def solution(word, pages):
    n = len(pages)

    urls = [''] * n
    extern_urls = [[] for _ in range(n)]
    scores = [{'basic':0, 'extern_link':0, 'link':[0,1]} for _ in range(n)]

    p_word = re.compile(f'[^a-zA-Z]{word}[^a-zA-Z]', re.I | re.S)
    p_head = re.compile(f'<head>.*</head>', re.I | re.S)
    p_head_meta_url = re.compile(f'<meta.*".*://.*"', re.I)
    p_url = re.compile(f'".*://.*"', re.I)
    p_body = re.compile(f'<body>.*</body>', re.I | re.S)
    p_a_url = re.compile(f'<a href="\S*"', re.I)

    for i in range(n):

        page_words_replaced = re.sub(f'[^a-zA-Z]{word}[^a-zA-Z]', f'=={word}==', pages[i], flags = re.I | re.S)
        page_words = p_word.findall(page_words_replaced)
        scores[i]['basic'] = len(page_words)

        page_head = p_head.search(pages[i])

        page_meta_url = p_head_meta_url.search(page_head.group())

        page_url = p_url.search(page_meta_url.group())
        urls[i] = page_url.group()[1:-1].split('://')[1]

        page_body = p_body.search(pages[i])

        tmp = re.sub(f'<a href=".*{urls[i]}"', '', page_body.group(), flags = re.I)
        page_extern_links = p_a_url.findall(tmp)
        page_extern_links = list(map(lambda x:x[:-1].split('://')[1], page_extern_links))
        extern_urls[i] = page_extern_links
        scores[i]['extern_link'] = len(page_extern_links)

    for i in range(n):
        for j in range(n):
            if i==j: continue
            if extern_urls[j].count(urls[i]) > 0:
                scores[i]['link'][0] = scores[i]['link'][0] * scores[j]['extern_link'] +  scores[j]['basic'] * scores[i]['link'][1]
                scores[i]['link'][1] *= scores[j]['extern_link']

    matching_scores = {i:scores[i]['basic'] + scores[i]['link'][0]/scores[i]['link'][1] for i in range(n)}

    return max(matching_scores.items(), key=lambda x:(x[1], -x[0]))[0]


print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>0muzi0Muzi0MUZI0\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
