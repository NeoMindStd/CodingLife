a, e = int(input()), int(input())
results = []

if a >= 3 and e <= 4: results.append('TroyMartian')
if a <= 6 and e >= 2: results.append('VladSaturnian')
if a <= 2 and e <= 3: results.append('GraemeMercurian')

print('\n'.join(results))
