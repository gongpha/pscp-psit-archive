'''Never call Saul'''
def main():
    '''I got push out of a Kayak! Better call Saul'''
    num_of_people = int(input())
    weight_list = input().split()
    weight_list = [int(i) for i in weight_list][:2*num_of_people]
    weight_list.sort()
    print(find_min_diff(weight_list))

def find_min_diff(num_list):
    '''Better call Saul'''
    temp_diff = []
    curr_diff = 10000
    for _ in range(0, len(num_list), 2):
        for i in range(len(num_list)-1):
            if abs(num_list[i+1] - num_list[i]) < curr_diff:
                curr_diff = abs(num_list[i+1] - num_list[i])
                one, two = num_list[i], num_list[i+1]
        num_list.remove(one)
        num_list.remove(two)
        temp_diff.append(curr_diff)
        curr_diff = 10000
    temp_diff.remove(max(temp_diff))
    return int(sum(temp_diff))

if __name__ == '__main__':
    main()
