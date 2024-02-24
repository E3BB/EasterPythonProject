
def clamp(num, minn, maxn):
    ret = num
    if num > maxn: ret = maxn
    if num < minn: ret = minn
    return ret
