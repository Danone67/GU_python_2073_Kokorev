with open ('nginx_logs.txt', encoding='utf-8') as logs:
    with open('task.txt', 'w', encoding='utf-8') as a:
        for line in logs:
            remote_addr = line[0:line.find('-')]
            request_type = line[line.find(']')+3:line.find('/d')]
            requested_resource = line[line.find('/d'):line.find('H')]
            pars = (remote_addr, request_type, requested_resource)
            a.write(' '.join(pars) + "\n")