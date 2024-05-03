def compareVersion(self, version1: str, version2: str) -> int:
    v1 = version1.split('.')
    v2 = version2.split('.')
    v1 = [i.lstrip('0') for i in v1]
    v2 = [i.lstrip('0') for i in v2]
    k = 1
    if len(v1)<len(v2):
        v1, v2 = v2, v1
        k = -1
    n2 = len(v2)
    for idx, v in enumerate(v1):
        if idx<n2:
            if v == '' and v2[idx] != '':
                return -k
            elif v != '' and v2[idx] == '':
                return k
            elif v == '' == v2[idx]:
                continue
            elif v != v2[idx]:
                return 1 if int(v)>int(v2[idx]) else -1
        else:
            if v == '':
                continue
            else:
                return k
    return 0
