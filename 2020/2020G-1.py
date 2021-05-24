"""
Google Kick Start - Round G 2020 - Q1 [SOLVED]
Daniel Cortild - 09/11/2020
"""

for T in range(int(input())):
  text = input()
  count = 0
  nbStart = text.count("START")
  for i in range(len(text)):
    if(text[i:i+4] == "KICK"):
      count += nbStart
    if(text[i:i+5] == "START"):
      nbStart -= 1

  print("Case #{}: {}".format(T+1, count))