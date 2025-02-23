class Solution:
    def dataTypeSize(self, str):
     sizes = {
         "Character": 1,
         "Integer": 4,
         "Long":8,
         "Float":4,
         "Double":8
     }
     return sizes[str] if str in sizes else -1
