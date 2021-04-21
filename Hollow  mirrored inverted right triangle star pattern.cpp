#include<iostream>

using namespace std;

int main(){
		
		int size;
		
		cin>>size;
		
		
		for(int i=0; i<size; i++){
			
			for(int j=0; j<i; j++){
				
				cout<<" ";
			}
				for(int j=i; j<size; j++){
					if(i==0 || j==i || j==size-1 ){
						
					cout<<"*";
					}else{
						cout<<" ";
					}
				}
				
				
			
			
					cout<<endl;
			
			
		}
		

		return 0;
}

