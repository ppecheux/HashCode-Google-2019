# def get_data():
#     file_name = "a_example.txt"
#     file_obj = open(file_name, "r+")
#     lines = file_obj.read().split("\n")
#     N = int(lines[0])
#     lines = lines[1:]
#     imgs = {}
#     for i,v in enumerate(lines):
#         imgs[i] = 
#     print(lines)

# get_data()












































def transition_evaluation(tags1= [1,2,4],tags2 = [2,3,4]):
    # common_tags= set(tags1).intersection(tags2)
    # print(common_tags)
    # unic_tags1= set(tags1).difference(tags2)
    # print(unic_tags1)
    # unic_tags2= set(tags2).difference(tags1)
    # print(unic_tags2)
    # score= min(len(common_tags),len(unic_tags1),len(unic_tags2))
    # print (score)
    return min(
        len(set(tags1).intersection(tags2)),
        len(set(tags1).difference(tags2)),
        len(set(tags2).difference(tags1)))

print(transition_evaluation())


