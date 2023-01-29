class LFUCache:
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.used = 0
      self.key = dict()
      self.ordered_count = dict()
      self.min_count = 0

    def get(self, key: int) -> int:
      val = -1
      if key in self.key:
        val = self.key[key][0]
        old_count = self.key[key][1]
        self.key[key][1] += 1
        del self.ordered_count[old_count][key]
        new_count = self.key[key][1]
        self._update_count_dict(key, val, new_count)
        if self.min_count == old_count and len(self.ordered_count[old_count]) == 0:
          self.min_count = new_count
      return val

    def put(self, key: int, value: int) -> None:
      if self.capacity <= 0: return

      if key in self.key:
        self.key[key][0] = value
        old_count = self.key[key][1]
        self.key[key][1] += 1
        new_count = old_count + 1
        del self.ordered_count[old_count][key]
        self._update_count_dict(key, value, new_count)
        if self.min_count == old_count and len(self.ordered_count[old_count]) == 0:
          self.min_count = new_count
      else:
        if self.used < self.capacity:
          self.key[key] = [value, 1]
          self._update_count_dict(key, value, 1)
          self.used += 1
          self.min_count = 1
        else:
          remove_key, remove_val = self.ordered_count[self.min_count].popitem(0)
          del self.key[remove_key]
          self.key[key] = [value, 1]
          self._update_count_dict(key, value, 1)
          self.min_count = 1

    def _update_count_dict(self, key: int, value: int, new_count: int) -> None:
      if new_count not in self.ordered_count: 
        self.ordered_count[new_count] = OrderedDict()
      self.ordered_count[new_count][key] = value
      self.ordered_count[new_count].move_to_end(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
