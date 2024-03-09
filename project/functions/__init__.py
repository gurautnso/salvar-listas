def arqexists(file_name):
    try:
        a = open(file_name, 'rt')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


