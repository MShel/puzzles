def simplifyPath(path):
    path_list = path.split('/')
    result = []
    for path in path_list:
        if path not in ['.','..'] and path:
            result.append(path)
        elif result and path == '..':
            result.pop()
    return '/'+'/'.join(result)
path =  "/home/a/./x/../b//c/"

print(simplifyPath(path))