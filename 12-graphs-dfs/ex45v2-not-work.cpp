/*#There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
#Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
#This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
#Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
#It's guaranteed that each city can reach city 0 after reorder.

#exercise 1466

#this solution was a first approach, but it doesn't work all the time
#we were triyng to do a graph and change the direction of each wrong path, but doing this brings many problems and low efficienty
*/

class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        int cant=0;

        for(int i = 0; i<n-1; i++){//start from each city
            dfs(connections, connections[i][0], cant, n);
        }
        return cant;
    }

    bool dfs(vector<vector<int>>& connections, int city, int & cant, int n){

            for (int i=0; i<n-1; i++){//let's find the city in the graph
                if(city == connections[i][0]){
                    if (dfs(connections, connections[i][1], cant, n)){
                        return true;
                    }else{ //if returns false it means this path did not arrive to the capital city, so we have to chage it's direction
                        connections[i][0] = connections[i][1];
                        connections[i][1]=city;
                        cant++;
                        return false;
                    }
                }else if (city == 0)
                        return true;
            }
            return false;

        //THIS SOLUTION IS CLOSE BUT IS INCORRECT, WAS ONLY A FIRST APPROACH
    }
};