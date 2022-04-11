# [1차] 캐시
# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

# 지도 개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을
# 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.

# LRU 캐시 알고리즘 - 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법
# https://gingerkang.tistory.com/26
# https://wlswoo.tistory.com/16
# 캐시 알고리즘 공부하기.

cacheSize = 3
reference = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cache = []
cnt = 0
for ref in reference:
  if not ref in cache: # cache miss 부분?
    cnt +=5
    if len(cache) < cacheSize:
        cache.append(ref)
    else:
        cache.pop(0)
        cache.append(ref)
  else: # cache Hit 부분인가?
    cache.pop(cache.index(ref))
    cache.append(ref)
    cnt+=1
# print(cache)
# print(cnt)
# 카카오 해설에서 그랬듯이 0 처리 문제인듯 6개중 2개 통과못함
# 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 
# 도시 이름은 최대 20자로 이루어져 있다.
# 대소문자 + 0처리.

def solution(cacheSize, cities):
    answer = 0
    cache = [] #결국 스택이랑 다를게 없나?
    for i in cities:
        if not i in cache: # cache miss
            answer+=5
            if len(cache) < cacheSize:
                cache.append(i.lower()) #cache 에 입력값 넣을떄 소문자로 넣어줌
            elif cacheSize ==0: #0일경우 그냥 넘어가고 answer만 더해주는.
                continue
            else:
                cache.pop(0)
                cache.append(i.lower())
        else:
            cache.pop(cache.index(i))
            cache.append(i.lower()) 
            answer+=1

    return answer
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) 
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# 입출력 2, 4번 오류 
# 대소문자 i 를 출력하면서 소문자로 바꾸고 그 다음 캐시에 추가해야겠다.

def solution(cacheSize, cities):
    answer = 0
    cache = [] #결국 스택이랑 다를게 없나?
    for i in cities:
        i = i.lower()
        if not i in cache: # cache miss
            answer+=5
            if len(cache) < cacheSize:
                cache.append(i) #cache 에 입력값 넣을떄 소문자로 넣어줌
            elif cacheSize ==0: #0일경우 그냥 넘어가고 answer만 더해주는.
                continue
            else:
                cache.pop(0)
                cache.append(i)
        else:
            cache.pop(cache.index(i))
            cache.append(i) 
            answer+=1

    return answer
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) 
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#21, 52