#include<iostream>

using namespace std;

int main(){
	int SIZE;
	cin>>SIZE; //10
	
	
	for(int i = 1; i<=SIZE; i++){
		for(int j = 1; j<i;j++){
			cout<<" ";
		}
		
		for(int j = 1; j<=SIZE;j++){
			cout<<"*";
		}
		cout<<endl;
	}
	
	
	
	
	
	return 0;
}
