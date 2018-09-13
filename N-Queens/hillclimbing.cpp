#include<iostream>
#include<vector>
#include<ctime>
#include<algorithm>
#include<cmath>
#define pb(i) push_back(i)
using namespace std;
vector<int> queens;
int n, conflicts, step = 0, pre_step = 0, dis;
int heuristic(vector<int> state) {
	int res = 0;
	for(int i=1; i < n; i++)
		for(int j = i+1; j <= n; j++) {
			if((i + state[i] == j + state[j]) || (i - state[i] == j - state[j])) res ++;
		}
	return res;
}
void print_res() {
	cout << step << "\t\t" << conflicts << endl;
}
void print_state() {
	for(int i = 1; i <= n; i++) cout << queens[i] << ' ';
}
bool prCurState() {
	int cur_conflicts = heuristic(queens);
	if(cur_conflicts == 0) return false;
	vector<int> next_state = queens;
	bool found_better_state = false;
	for(int i = 1; i < n; i++) {
		for(int j = i + 1; j <= n; j++) {
			if(conflicts == 0) return false;
			if(step - pre_step == dis){
				print_res();
				pre_step = step;
			}
			step++;
			swap(next_state[i], next_state[j]);
			int temp_conflicts = heuristic(next_state);
			if(temp_conflicts < conflicts) {
				queens = next_state;
				conflicts= temp_conflicts;
				found_better_state = true;
			}
			swap(next_state[i], next_state[j]);
		}
		
	}
	if(found_better_state) return true;
	return false;
}
void initial() {
	queens.pb(0);
	for(int i = 1; i <= n; i++)
		queens.pb(i);
	int gt = 1;
	for(int i = 1; i <= n; i++){
		int j = rand() % n + 1;
		swap(queens[i], queens[j]);
	}
}
main()
{
	srand(time(NULL));
	n = 100;
	dis = 1000;
	initial();
	conflicts = heuristic(queens);
	cout << "Step\t\tConflicts\n";
	print_res();
	while(prCurState() == true) {
	}
	print_res();
	cout << "Best State :\n";
	cout << "Step : " << step << " ; Conflicts = " << conflicts << endl;
	print_state();
}

