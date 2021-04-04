#include<iostream>

using namespace std;

int main(){
	
	int num,max=0;
	// 23453 
	
	cin>>num;
	
	for(;num>0;num/=10){
		
		
		if(num%10>max){
			max=num%10;
			
		}
	}
	cout<<max;
	
	
	
	
	
	
	
	
	
	
	return 0;
}
