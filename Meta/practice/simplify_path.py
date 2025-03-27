
cwd = "/users/papamidnight/local/bin"
cd = "../app"

def simplify_path(cwd, cd):
    if cd.startswith('/'):
        path = cd
    else:
        path = cwd + '/' + cd if cwd.endswith('/') else cwd + '/' + cd

    components = path.split('/')

    result = []

    for component in components:
        if component == '' or component == '.':

            continue

        elif component == '..':
            if result:
                result.pop()
        
        else:
            result.append(component)

    final_path = '/' + '/'.join(result)

    return final_path

print(simplify_path(cwd, cd))