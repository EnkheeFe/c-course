#include<iostream>

using namespace std;

int main(){
	
	int n,num=0;
	// 234-> 2+3+4=9
	cin>>n;
	
	for(;n>0;n/=10){
		if(n%2!=0){
		
		num=num+1;
	}
	}
	
	cout<<num;
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
