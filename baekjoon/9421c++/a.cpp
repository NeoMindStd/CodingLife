#include <stdio.h>
#include <set>

using namespace std;

int p_len = -1;

int* Eratos(int n)
{
	if (n <= 1) return NULL;

	bool* PrimeArray = new bool[n + 1];

	for (int i = 2; i <= n; i++)
		PrimeArray[i] = true;

	for (int i = 2; i * i <= n; i++)
	{
		if (PrimeArray[i]) {
			for (int j = i * i; j <= n; j += i)
			{
				PrimeArray[j] = false;
			}
		}
	}

	p_len = 0;
	for (int i = 2; i <= n; i++)
		if (PrimeArray[i])
			p_len++;

	int* primes = new int[p_len];
	int idx = 0;
	for (int i = 2; i <= n; i++)
	{
		if (PrimeArray[i])
			primes[idx++] = i;
	}
	return primes;
}

int main()
{
	int n;
	scanf_s(" %d", &n);
	int* pri = Eratos(n);
	for (int i = 0; i < p_len; i++) {
		printf("%d\n", pri[i]);
	}

	set<int> sp(pri, pri + p_len);

	for (set<int>::iterator iter = sp.begin(); iter != sp.end(); ++iter) {
		printf("%d\n", *iter);
	}

	set<int> sang;
	set<int> exp;
	/*
	for num in pri :
		if num in sang | exp :
			continue
		tmp = set()
		tn = num
		while True :
			tmp.add(tn)
			tn = sum([int(i)**2 for i in list(str(tn))])
			if tn == 1 :
				sang |= tmp & sp
				break
			if tn in tmp :
				exp |= tmp
				break
		sang = list(sang)
		sang.sort()
		print("\n".join(map(str, sang)))
		*/
}