info = [int(input()) for _ in range(4)]

processed = [info[i+1]-info[i] for i in range(3)]
if min(processed) > 0: print('Fish Rising')
elif max(processed) < 0: print('Fish Diving')
elif min(processed) == max(processed) == 0: print('Fish At Constant Depth')
else: print('No Fish')
