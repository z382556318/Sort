import random
import time
class Sort:
    def bubbleSort(self, array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

    def exchangeSort(self, array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]

    def insertSort(self, array):
        for i in range(1,len(array)):
            if array[i - 1] > array[i]:
                tmp = array[i]
                j = i - 1
                while array[j] > tmp and j >= 0:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = tmp

    def insertSort_new(self, array):
        for i in range(len(array)):
            for j in range(i):
                if array[j] > array[i]:
                    array.insert(j, array.pop(i))
                    break

    def shellSort(self, array):
        n = len(array)
        gap = n // 2
        while gap != 0:
            for i in range(gap):
                for j in range(i, n - gap, gap):
                    if array[j + gap] < array[j]:
                        tmp = array[j + gap]
                        k = j
                        while array[k] > tmp and k >= i:
                            array[k + gap] = array[k]
                            k -= gap
                        array[k + gap] = tmp
            gap = gap // 2

    def selectSort(self, array):
        for i in range(len(array)):
            min = i
            for j in range(i,len(array)):
                if array[j] < array[min]:
                    min = j
            array[i], array[min] = array[min], array[i]

    def partition(self, array, left, right):
        sign = array[left]
        while left < right:
            while left < right and array[right] >= sign:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= sign:
                left += 1
            array[right] = array[left]
        array[left] = sign
        return left

    def quickSort(self, array, left, right):
        if left < right:
            p = self.partition(array, left, right)

            self.quickSort(array, left, p)
            self.quickSort(array, p + 1, right)

    def quickSortWithoutRecursion(self, array):
        # 使用栈实现快速排序
        stack = []
        stack.append(0)
        stack.append(len(array) - 1)
        while stack:
            high = right = stack.pop()
            low = left = stack.pop()
            if low == high:
                continue
            left = self.partition(array, left, right)
            if left - 1 > low:
                stack.append(low)
                stack.append(left - 1)
            if left + 1 < high:
                stack.append(left + 1)
                stack.append(high)

    def mergSort(self, array):
        def merge(arr_l, arr_r):
            result = []
            while len(arr_l) and len(arr_r):
                if arr_l[0] < arr_r[0]:
                    result.append(arr_l.pop(0))
                else:
                    result.append(arr_r.pop(0))
            else:
                if len(arr_l):
                    result.extend(arr_l)
                else:
                    result.extend(arr_r)
            return result

        def merge_sort(array):
            length = len(array)
            if length == 1:
                return array
            n = length // 2
            arr_l = merge_sort(array[:n])
            arr_r = merge_sort(array[n:])
            return merge(arr_l, arr_r)

        return merge_sort(array)

    def heapSort(self, array):
        def heap_sort(ary):
            # 节点数
            n = len(ary)
            # 最后一个有子节点的节点（最后一个非叶节点）
            first = n // 2
            for start in range(first, -1, -1):
                # 对每一个非叶子节点倒序进行堆调整
                heap_adjust(ary, start, n - 1)
            for end in range(n - 1, 0, -1):
                # 交换最后一个叶节点和根节点
                ary[0], ary[end] = ary[end], ary[0]
                # 对新的堆栈进行调整
                heap_adjust(ary, 0, end - 1)

        def heap_adjust(ary, start, end):
            root = start
            while True:
                # 因为数组计数是从0开始，所以下式代表其左孩子
                child = 2 * root + 1
                # 左孩子超出数组范围：跳出
                if child > end: break
                # 挑选左右孩子中更大者
                if child + 1 <= end and ary[child] < ary[child + 1] :
                    child += 1
                # 交换双亲和子节点
                if ary[root] < ary[child]:
                    ary[root], ary[child] = ary[child], ary[root]
                    root = child
                else:
                    break
        heap_sort(array)


if __name__ == '__main__':
    srt = Sort()
    list = [random.randint(1, 999) for i in range(10000)]

    start = time.clock()
    list_true = sorted(list)
    end = time.clock()
    print("函数sorted排序   ", end - start, '\n')

    list1 = list.copy()
    start = time.clock()
    srt.quickSort(list1, 0, len(list1) - 1)
    end = time.clock()
    print("快速排序         ", end - start)
    print("排序结果         ", list1 == list_true, '\n')

    list2 = list.copy()
    start = time.clock()
    srt.quickSortWithoutRecursion(list2)
    end = time.clock()
    print("非递归快速排序   ", end - start)
    print("排序结果         ", list2 == list_true, '\n')

    list3 = list.copy()
    start = time.clock()
    srt.bubbleSort(list3)
    end = time.clock()
    print("冒泡排序         ", end - start)
    print("排序结果         ", list3 == list_true, '\n')

    list4 = list.copy()
    start = time.clock()
    srt.exchangeSort(list4)
    end = time.clock()
    print("交换排序         ", end - start)
    print("排序结果         ", list4 == list_true, '\n')

    list5 = list.copy()
    start = time.clock()
    srt.insertSort(list5)
    end = time.clock()
    print("插入排序         ", end - start)
    print("排序结果         ", list5 == list_true, '\n')

    list6 = list.copy()
    start = time.clock()
    srt.insertSort_new(list6)
    end = time.clock()
    print("新插入排序       ", end - start)
    print("排序结果         ", list6 == list_true, '\n')

    list7 = list.copy()
    start = time.clock()
    srt.shellSort(list7)
    end = time.clock()
    print("希尔排序         ", end - start)
    print("排序结果         ", list7 == list_true, '\n')

    list8 = list.copy()
    start = time.clock()
    srt.selectSort(list8)
    end = time.clock()
    print("选择排序         ", end - start)
    print("排序结果         ", list8 == list_true, '\n')

    list9 = list.copy()
    start = time.clock()
    list9 = srt.mergSort(list9)
    end = time.clock()
    print("归并排序         ", end - start)
    print("排序结果         ", list9 == list_true, '\n')

    list10 = list.copy()
    start = time.clock()
    srt.heapSort(list10)
    end = time.clock()
    print("堆排序           ", end - start)
    print("排序结果         ", list10 == list_true, '\n')
