#include<iostream>
using namespace std;

int main() {
	
	
	int o,t,m,s;
	
	cin>>o;
	
	t=o/3600;
	m=(o-t*3600)/60;
	s=o-(t*3600+m*60);
	cout<<t<<" "<<m<<" "<<s;
	
	

	return 0;
}
