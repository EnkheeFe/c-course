#include<iostream>

using namespace std;

int main(){
	
	int n,i;
	cin>>n; // 16
	
	for(;n>=2 && n%2==0;n/=2){
		i=n/2; //16:2->8
		
	}if(i==1){
		cout<<"YES";
	}else{
		cout<<"NO";
	}
	
	
	

	
	return 0;
}
