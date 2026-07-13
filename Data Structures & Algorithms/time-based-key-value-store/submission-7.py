class TimeMap:

    def __init__(self):
        self.hash_store_key = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        hash_store_key = self.hash_store_key
        hash_store_key[(key,timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        hash_store_key = self.hash_store_key
        if (key, timestamp) in hash_store_key:
            return hash_store_key[(key, timestamp)]
        else:
            # binary search since already sorted
            hash_list = list(hash_store_key.items())
            filtered_list = [k for k in hash_list if k[0][0]==key]
            length = len(filtered_list)
            low = 0
            high = length - 1
            # hash_list = list(hash_store_key.items())
            # filtered_list = [k for k in hash_list if k[0][0]==key]
            print(filtered_list)
            if len(filtered_list) ==0: return ""
            time_first = filtered_list[0][0][1] 
            if time_first > timestamp:
                return ""
            if (length ==1):
                # time = hash_list[0][0][1] 
                # if time < timestamp:
                return hash_store_key[(key, filtered_list[0][0][1])]
                # else: return ""
            while low<high:
                mid = (low+high)//2
                item = filtered_list[mid]
                time_mid = item[0][1]
                print(time_mid)
                if mid == low:
                    item2 = filtered_list[mid+1]
                    time_mid2 = item2[0][1]
                    if time_mid2 < timestamp:
                        if (key, time_mid2) in hash_store_key:
                            return hash_store_key[(key, time_mid2)]
                        else: return ""
                    else:
                        if (key, time_mid) in hash_store_key:
                            return hash_store_key[(key, time_mid)]
                        else: return ""
                if time_mid > timestamp:
                    high = mid
                    continue
                else:
                    low = mid
                    continue
            return ""


