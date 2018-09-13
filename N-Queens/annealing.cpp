#include<iostream>
#include<vector>
#include<ctime>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#define pb(i) push_back(i)
using namespace std;
vector<int> queens;
int n, conflicts, step = 0, pre_step = 0, dis, init_times = 0;
float p = 0.99;
bool annealing(int delta_E) {
	p = min(1.0f, exp(delta_E/p));
	int pivot = p*100;
	int k = rand() % 100;
	if(k < pivot) return true;
	return false;
}
int heuristic(vector<int> state) {
	int res = 0;
	for(int i=1; i < n; i++)
		for(int j = i+1; j <= n; j++) {
			if((i + state[i] == j + state[j]) || (i - state[i] == j - state[j])) res ++;
		}
	return res;
}
void initial() {
	init_times ++;
	queens.clear();
	queens.pb(0);
	for(int i=1; i <= n; i++)
		queens.pb(i);
	int gt = 1;
	for(int i = 2; i < n; i++) {
		if(gt > 100000) {
			gt = 100000;
			break;
		}
		else gt *= i;
	}
	int k = rand() % gt;
	k ++;
	for(int i = 1; i <= k; i++)
		next_permutation(&queens[1], &queens[n]);
	conflicts = heuristic(queens);
}

void print_res() {
	cout << step << "\t\t" << conflicts << "\t\t\t" << init_times << endl;
}
bool prCurState() {
	int cur_conflicts = heuristic(queens);
	if(cur_conflicts == 0) return false;
	vector<int> next_state = queens;
	int des = n*sqrt(n);
	for(int p = 1; p <= des; p++) {
		if(step - pre_step == dis) {
			print_res();
			pre_step = step;
		}
		step++;
		int i = rand() % n + 1;
		int j = rand() % n + 1;
		swap(next_state[i], next_state[j]);
		int temp_conflicts = heuristic(next_state);
		if(temp_conflicts < conflicts) {
			conflicts = temp_conflicts;
			queens = next_state;
			return true;
		}
		else {
			bool acceptance = annealing(conflicts - temp_conflicts);
			if(acceptance) {
				conflicts = temp_conflicts;
				queens = next_state;
				return true;
			}
		}
		swap(next_state[i], next_state[j]);
	}
	return false;
}
main()
{
	srand(time(NULL));
	n = 100;
	dis = 100;
	cout << "Step\t\tConflicts\t\tInitial\n";
	initial();
	print_res();
	while(true) {
		prCurState();
		if(conflicts == 0) break;
	}
	print_res();
	cout << "Best Found State :\n";
	cout << "Step : " << step << " ; Conflicts = " << conflicts << " ; Initial : " << init_times;
}

