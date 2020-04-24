class OrderedSorting(object):
    def __init__(self):
        # pass
        self.test()

    def sort_in_order(self,arr2,arr1):
        temp ={i:index for index,i in enumerate(arr1)}
        need_to_sort = []
        for i in arr2:
            if i not in temp:
                need_to_sort.append(i)
            else:
                arr1[temp[i]]=i
                del temp[i]
        arr1 += sorted(need_to_sort)
        for i in temp:
            del arr1[i]
        return arr1

    def test(self):
        if self.sort_in_order([1,2,3,4,5],[5,4,2]) == [5, 4, 2, 1, 3]:
            print("passed testcase 1")
        if self.sort_in_order([5,17,100,11],[100,1]) == [100, 5, 11, 17]:
            print("passed testcase 2")

if __name__ == "__main__":
    OrderedSorting()