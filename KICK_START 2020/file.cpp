#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;
typedef long long LL;

const int N = (int) 1e6 + 6, mod = (int) 0;
int a[N];
long long sum[N];
int main() {
	ios_base::sync_with_stdio(0);
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		int n, p,k,max=0,index=-1,sum=0;
		cin >> n >> p>>k;
		int limit=n;
		for (int l=0;l<n;l++){
		for (int j = 0; j < k;j++)
			cin >> a[j];
		for (int j = 0; j < k; j++)
			if(max<a[j] && a[j]+1>=max){
			    index=j;
			}
			else{
			    break;
			}
		int j=0;
		while(j<=index && limit!=0){
		    if(j<=limit){
		        sum+=a[j];
		        limit-=1;
		    }
		    else{
		        break;
		        
		    }
		}
		}
		cout << sum << '\n';
	}
}