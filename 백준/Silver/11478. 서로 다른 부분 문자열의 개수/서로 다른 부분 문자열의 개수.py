import sys

sub_string = set()
s = sys.stdin.readline().rstrip()
sub_string.add(s)
for str_num in range(1, len(s)+1):
    for i in range(0, len(s)-str_num+1):
        sub_string.add(s[i:i+str_num])

print(len(sub_string))