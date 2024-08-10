/*
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

exercise 841
*/

#include <vector> 
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> visitados(rooms.size(), false);

        int cant = 0;

        recursive(rooms, 0, visitados, cant);

        return (cant == rooms.size());
    }

private:
    void recursive(vector<vector<int>>& rooms, int ini, vector<bool>& visitados, int &cant) {
        visitados[ini] = true;
        cant++;
        for (int ady : rooms[ini]) {
            if (!visitados[ady]) {
                recursive(rooms, ady, visitados, cant);
            }
        }
    }
};
