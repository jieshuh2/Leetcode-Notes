array = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
def count(array):
    dic = {}
    for info in array:
        count, domain = info.split(" ")
        count = int(count)
        domains = domain.split(".")
        for idx, dom in enumerate(domains):
            name = ".".join(domains[idx:])
            if name not in dic:
                dic[name] = 0
            dic[name] += count
    res = []
    for domain in dic:
        res.append(str(dic[domain]) + " " + domain)
    return res
print(count(array))