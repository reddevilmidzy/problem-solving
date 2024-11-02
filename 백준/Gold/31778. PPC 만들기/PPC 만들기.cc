#include <iostream> 
#include <stack>
#include <queue>
#include <cstring>
using namespace std; 

long long p_count[200001];

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL); 
	cout.tie(NULL); 

	int n, k; cin >> n >> k; 
	string s; cin >> s; 
	stack<int> st;  
	queue<int> q;
	for (int i = 0; i < n; i++) {
		if (s[i] == 'C') {
			q.push(i);
		}
		else {
			st.push(i);
		}
	}

	for (int i = 0; i < k; i++) {
		if (st.empty() || q.empty()) {
			break;
		}
		int p_index = st.top(); 
		st.pop();
		int c_index = q.front();
		q.pop();

		if (p_index < c_index) {
			break;
		}
		
		// swap 
		s[p_index] = 'C'; 
		s[c_index] = 'P';
	}

	long long ret = 0;
	for (int i = 0; i < n; i++) {
		if (i != 0) {
			p_count[i] = p_count[i - 1]; 
		}
		if (s[i] == 'P') {
			p_count[i]++;
		}
		else {
		    ret += (p_count[i] * (p_count[i] - 1)) / 2;
		}
	}
	cout << ret << endl;
	return 0;
}