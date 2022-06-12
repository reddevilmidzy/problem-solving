#include<stdio.h>

int main(void) {
	int num[1000];
	int k;
	int n;
	int cnt = 0;

	scanf("%d %d", &n, &k);

	for (int i = 2; i <= n; i++)
		num[i] = i;

	for (int i = 2; i <= n; i++)
	{
		//printf("%d %d %d", i, n, cnt);
		if (num[i] == 0)
			continue;
		else
		{
			for (int j = i; j <= n; j += i) {
				if (num[j] != 0) {
					num[j] = 0;
					cnt++;
				}
				if (cnt == k)
				{
					printf("%d", j);
					break;
				}
			}
		}
	}
	return 0;
}