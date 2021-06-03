#!/usr/bin/env python3

def lower_en(char,k):
    ascii_char = ord(char)
    ascii_char += k % 26
    if not ascii_char <= 122:
        distance = ascii_char - 122
        position = 97 + (distance - 1)
        return chr(position)
    else:
        return chr(ascii_char)

def upper_en(char,k):
    ascii_char = ord(char)
    ascii_char += k % 26
    if not ascii_char <= 90:
        distance = ascii_char - 90
        position = 65 + (distance - 1)
        return chr(position)
    else:
        return chr(ascii_char)

def main(s, k):
  encrypted = ""
  for i in range (0,len(s)):
    en_char = ""
    char = s[i]
    if 65 <= ord(char) <= 90:
      en_char = upper_en(char, k)
    elif 97 <= ord(char) <= 122:
      en_char = lower_en(char, k)
    else:
      en_char = char
    encrypted += en_char
  return encrypted
