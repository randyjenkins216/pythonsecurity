import dns.resolver

pointtodomain = 'youtube.com'
recordtype = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA']

resolver = dns.resolver.Resolver()
for i in recordtype:
    try: 
        answer = resolver.resolve(pointtodomain, recordtype)
    except dns.resolver.NoAnwer:
        continue
    print(f'{recordtype} records for {pointtodomain}')
    for r in answer:
        print(f'{r}')