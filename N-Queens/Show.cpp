#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
main()
{
	vector<int> a;
	int n, t;
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	while(ifs >> t) {
		a.push_back(t);
	}
	for(int i = 0; i < a.size(); i++) {
		for(int j = 0; j < a.size(); j++) {
			if(j == a[i]-1) ofs << "x ";
			else ofs << ". ";
		}
		ofs << endl;
	}
}

