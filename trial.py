import textwrap
your_string = "123456789gretwhehtthdsfsdfdsfdsssthttrhtwhtr"
print(textwrap.wrap(your_string, 5))
n=len(your_string)//5+1
parts = [your_string[i:i+n] for i in range(0, len(your_string), n)]
print(parts)