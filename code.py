def get_data():
    file_name = "a_example.txt"
    file_obj = open(file_name, "r+")
    lines = file_obj.read().split("\n")
    N = int(lines[0])
    lines = lines[1:]
    imgs = {}
    for i,v in enumerate(lines):
        imgs[i] = 
    print(lines)

get_data()


