#include<iostream>

using namespace std;

int main(){
	
	int n,even, sum=0;
	// 234-> 2+3+4=9
	cin>>n;
	
	for(;n>0;n/=10){
		if(n%2==0){
		
		sum=sum+n%10;
	}
	}
	
	cout<<sum;
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
