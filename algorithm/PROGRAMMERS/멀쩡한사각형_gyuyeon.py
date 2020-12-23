# w와 h의 최대공약수를 구하자
# 최대공약수가 1이면:
# w*h - (w + h - 1)
# 최대공약수가 1보다 크면:
# w*h - (최대공약수*(w//최공+h//최공-1))
def gcm(w, h):
    g = 1
    for k in range(2, min(w, h) + 1):
        while (w % k == 0) & (h % k == 0):
            w = w // k
            h = h // k
            g = g * k
    return g


def solution(w, h):
    gg = gcm(w, h)
    if gg == 1:
        answer = w * h - (w + h - 1)
    else:
        answer = w * h - (gg * (w // gg + h // gg - 1))

    return answer