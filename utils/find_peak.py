def findPeak(list_with_peaks):
    start, end = 1, len(list_with_peaks) - 2
    print((start, end))

    while start + 1 < end:
        mid = start + (end - start) / 2
        print (mid)
        if list_with_peaks[mid] > list_with_peaks[mid - 1] and list_with_peaks[mid] < list_with_peaks[mid + 1]:
            start = mid
        elif list_with_peaks[mid] < list_with_peaks[mid - 1] and list_with_peaks[mid] > list_with_peaks[mid + 1]:
            end = mid
        elif list_with_peaks[mid] > list_with_peaks[mid - 1] and list_with_peaks[mid] > list_with_peaks[mid + 1]:
            return mid
        else:
            start = mid  # or end = mid

    if list_with_peaks[start] < list_with_peaks[end]:
        return end

    return start

print(findPeak([1,1,1,7,3,4,5,9,11,125]))