a, b = int(input()), int(input())

def fine(a, b):
    if b - a <= 20: return 100
    if b - a <= 30: return 270
    return 500

print(f'You are speeding and your fine is ${fine(a, b)}.' if a < b else 'Congratulations, you are within the speed limit!')
