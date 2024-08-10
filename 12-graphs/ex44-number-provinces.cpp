/*
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

exercise 547
*/

#include <vector> 
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int result = 0;
        vector<bool> visitados(isConnected.size(), false);

        for(int i=0; i<isConnected.size(); i++){
            if(!visitados[i]){
                recursive(isConnected, i, visitados);
                result++;
            }
        }

        return result;
    }
private:
    void recursive(vector<vector<int>>& isConnected, int ini, vector<bool>& visitados){
        visitados[ini] = true;
         for (int i=0; i<isConnected[ini].size(); i++){
            if(isConnected[ini][i]==1 && !visitados[i]){
                recursive(isConnected, i, visitados);
            }
         }
    }
};