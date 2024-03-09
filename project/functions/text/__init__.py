def arqexists(file_name):
    try:
        a = open(file_name, 'rt')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def arqcreate(file_name):
    a = open(file_name, 'wt+')
    a.close()


def arqwrite(file_name, prompt):
    a = open(file_name, 'at')
    a.write(prompt)
    a.close()


def arqread(file_name):
    a = open(file_name, 'rt')
    nums = []
    for c in a:
        nums.append(c.split(';'))
    try:
        number = int(nums[-1][0])
        a.close()
    except:
        a.close()
        return 0
    else:
        return number
