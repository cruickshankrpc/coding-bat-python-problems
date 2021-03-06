# * STRING-2:

'''
Given a string, return a string where for every char in the original, 
there are two chars. 
'''
def double_char(str):
  new_str = ""
    for char in str:
      new_str += char*2
    return new_str

'''
Return the number of times that the string "hi" appears anywhere 
in the given string. 
'''

def count_hi(str):
  return str.count("hi")

'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''

def cat_dog(str):
  # catcount=0
  # dogcount=0
  # for i in range(len(str)) :
  #   if str[i] == "cat" :
  #     catcount = catcount + 1
  #   if str[i] == "dog" :
  #     dogcount = dogcount + 1
  # if dogcount == catcount :
  #   return catcount, dogcount
  
  return str.count("cat") == str.count("dog")

print(cat_dog('catcat'))

'''
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''

def count_code(str):
  count = 0 
  for i in range(len(str) - 3) : 
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e' :
      count = count + 1
  return count


'''
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''
def end_other(a, b):
  a2 = a.lower()
  b2 = b.lower()
  if b2[-len(a2):] == a2 or a2[-len(b2):] == b2 :
    return True 
  else :
    return False


'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
def xyz_there(str):
  for i in range(len(str)-2) :
    if str[i: i+3] == "xyz" and str[i-1] != "." :
      return True 
  return False

  # OR
  # return str.count("xyz") > str.count(".xyz")

