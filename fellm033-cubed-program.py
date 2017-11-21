def cubed(x,y=3):
    value = x**y
    return value
mf = open('input.txt')
mf_read = mf.read().splitlines()
print(str(mf_read))
mf_int = [int(i) for i in mf_read]
print(mf_int)
mf_cube = []
for i in mf_int:
    mf_cube.append(cubed(i))
mf_str = [str(i) for i in mf_cube]
print(mf_cube)
with open ('cubed.txt', mode = 'wt', encoding = 'utf-8') as cubed:
    cubed.write('\n'.join(mf_str))
