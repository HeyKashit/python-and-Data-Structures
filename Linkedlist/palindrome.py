class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1 = ''
        h1 = head
        while h1:
          str1 = str1 + str(h1.val)
          h1=h1.next
        return str1 == str1[::-1]
