#include<bits/stdc++.h>
#define pb(i) push_back(i)
using namespace std;
vector<int> queens;
int n, conflicts, step = 0, pre_step = 0, dis, init_times = 0;
vector<int> d_pos;
vector<int> d_neg;
int heuristic() {
	int res = 0;
	for(int i = 1; i <= 2*n - 1; i++) {
		if(d_pos[i] > 0) res += (d_pos[i] - 1);
		if(d_neg[i] > 0) res += (d_neg[i] - 1);
	}
	return res;
}
void swap_queens(int u, int v) {
	d_pos[u - queens[u] + n] --;
	d_pos[u - queens[v] + n] ++;
	d_neg[u + queens[u]] --;
	d_neg[u + queens[v]] ++;
	
	d_pos[v - queens[v] + n] --;
	d_pos[v - queens[u] + n] ++;
	d_neg[v + queens[v]] --;
	d_neg[v + queens[u]] ++;
	swap(queens[u], queens[v]);
}
void initial() {
	init_times ++;
	for(int i = 1; i <= n; i++)
		queens[i] = i;
	for(int i = 1; i <= n; i++) {
		int k = rand() % n + 1;
		swap(queens[1], queens[k]);
	}
	for(int i = 1; i <= 2*n-1; i++) {
		d_pos[i] = 0;
		d_neg[i] = 0;
	}
	for(int i = 1; i <= n; i++) {
		d_pos[i-queens[i]+n]++;
		d_neg[i+queens[i]]++;
	}
	conflicts = heuristic();
}

void print_res() {
	cout << step << "\t\t" << conflicts << "\t\t\t" << init_times << endl;
}
void print_state() {
//	for(int i = 1; i <= n; i++) cout << queens[i] << ' ';
	freopen("output.txt","w",stdout);
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			if(j == queens[i]) cout << "*";
			else cout << ".";
		}
		cout << endl;
	}
}
bool prCurState() {
	int cur_conflicts = heuristic();
	if(cur_conflicts == 0) return false;
	int des = n*sqrt(n);
	for(int p = 1; p <= des; p++) {
		if(step - pre_step == dis) {
			print_res();
			pre_step = step;
		}
		step++;
		int i = rand() % n + 1;
		int j = rand() % n + 1;
		swap_queens(i, j);
		int temp_conflicts = heuristic();
		if(temp_conflicts < conflicts) {
			conflicts = temp_conflicts;
			return true;
		}
		swap_queens(i, j);
		
	}
	return false;
}
main()
{
	srand(time(NULL));
	n = 1000;
	dis = 1000;
	queens.pb(0);
	for(int i=1; i <= n; i++)
		queens.pb(i);
	for(int i = 1; i <= 2*n; i++) {
		d_pos.pb(0);
		d_neg.pb(0);
	}
	cout << "Step\t\tConflicts\t\tInitial\n";
	initial();
	while(true) {
		if(prCurState() == false) initial();
		if(conflicts == 0) break;
	}
	print_res();
	cout << "\nBest State :\n";
	cout << "Step : " << step << " ; Conflicts = " << conflicts << " ; Initial : " << init_times << endl;
	print_state();
}

