#include<iostream>

using namespace std;

int main(){
	
	int n,i,s;
	cin>>n;
	for(i=1,s=1;s<n;i++){
		s=s*i;
	} if(s==n){
		i=i-1;
		cout<<i;
	}else{
		cout<<"NO";
	}
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
