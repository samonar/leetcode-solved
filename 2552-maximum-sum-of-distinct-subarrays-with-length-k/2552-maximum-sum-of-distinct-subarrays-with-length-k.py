class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()  # Melacak elemen unik
        current_sum = 0
        max_sum = 0
        begin = 0

        for end in range(len(nums)):
            # Jika elemen duplikat ditemukan, geser begin hingga elemen unik
            # print(f'end {nums[end]}:{end}, begin {nums[begin]}:{begin}, elemen {elements}, sum {current_sum}')
            while nums[end] in elements:
                elements.remove(nums[begin])
                current_sum -= nums[begin]
                begin += 1
            
            # Tambahkan elemen baru
            elements.add(nums[end])
            current_sum += nums[end]

            # Jika panjang jendela mencapai k, periksa max_sum
            if end - begin + 1 == k:
                max_sum = max(max_sum, current_sum)
                # Geser jendela
                elements.remove(nums[begin])
                current_sum -= nums[begin]
                begin += 1
           

        return max_sum
