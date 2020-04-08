from typing import List


class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    obj = {}

    # Count all nums
    for item in nums:
      if not item in obj:
        obj[item] = 1
      else:
        obj[item] += 1

    # obj = {
    #   1: 3
    #   2: 2
    #   3: 1
    # }

    # Make Array<Object> structure
    keys = list(map(lambda item: {'key': item, 'value': obj[item] }, list(obj.keys())))

    # keys = [{
    #   key: 2,
    #   value: 2
    # }, {
    #   key: 1,
    #   value; 3
    # }, {
    #   key: 3,
    #   value: 1
    # }]

    # Sort by value key (item['value'])
    keys.sort(key=lambda item: item['value'], reverse=True)

    return [keys[index]['key'] for index in range(k)]


my = Solution()
n0 = [1, 1, 1, 2, 2, 3]
k0 = 2
n1 = [4,1,-1,2,-1,2,3]
k1 = 2

ans = my.topKFrequent(n0, k0)
# ans = my.topKFrequent(n1, k1)
print("ans", ans)
