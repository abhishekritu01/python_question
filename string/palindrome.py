
# def isPalindrome(str):
#     if len(str) <= 1:
#         return True
#     else:
#         return str[0] == str[-1] and isPalindrome(str[1:-1])
    
# print(isPalindrome('abcba'))


def isPalindrome(str):
     for i in range(0, int(len(str)/2)):
         if str[i] != str[len(str)-i-1]:
              return False
         else:
              return True

print(isPalindrome('abcba'))