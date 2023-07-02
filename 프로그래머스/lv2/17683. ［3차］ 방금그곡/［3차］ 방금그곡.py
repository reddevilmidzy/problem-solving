def formatting(song): # 문자열 포맷후 리스트로
    res = []
    for i in range(len(song)):
        if song[i] != "#":
            res.append(song[i])
        else:
            res.append(res.pop()+song[i])
    return res

def delta(st, ed):
    st_h, st_m = map(int, st.split(":"))
    ed_h, ed_m = map(int, ed.split(":"))
    return (ed_h*60+ed_m) - (st_h*60+st_m)

def solution(m, musicinfos):
    answer = []
    song = formatting(m)
    idx = 0
    for char in musicinfos:
        st,ed,name,melody = char.split(",")
        play = delta(st, ed) # 실제 재생 시간 
        melo = formatting(melody)
        
        if play > len(melo): # 반복 발생
            real = melo*(play // len(melo)) + melo[:play%len(melo)]
        else:
            real = melo[:play]
            
        if "|"+"|".join(song)+"|" in "|"+"|".join(real)+"|":
            answer.append([-play, idx, name])
        idx += 1
    if not answer:
        return "(None)"
    
    answer.sort()
    return answer[0][2]