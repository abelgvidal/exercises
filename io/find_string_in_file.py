import mmap
import timeit

def text_in_file(text, filepath):
    """ is given "text" in file ? """
    with open(filepath, 'rb', 0) as file, mmap.mmap(
            file.fileno(),
            0,
            access=mmap.ACCESS_READ) as s:
        return (s.find(text.encode()) != -1)

def text_in_file2(text, filepath):
    return text in open(filepath).read()    

