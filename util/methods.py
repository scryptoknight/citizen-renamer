def open_main_window(parent, child, path):
    if path:
        child(path)
        parent.destroy()
    return


def path_open(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
