n, m = map(int, input().split())
a_arr = set(map(int, input().split()))
b_arr = set(map(int, input().split()))

aminusb = a_arr - b_arr
bminusa = b_arr - a_arr

for b in bminusa:
    aminusb.add(b)
print(len(aminusb))