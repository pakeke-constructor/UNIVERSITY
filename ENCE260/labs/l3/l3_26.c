


#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>

bool isWonRow(char player, const char game[3][3], uint8_t i)
{
    const char* row = game[i];
    bool won = true;
    for (int j=0; j<3; j++) {
        won = won && (row[j] == player);
    }

    return won;
}


int main(){
const char game[3][3] = {{'X', 'O', ' '},{'X', 'X', 'X'}, {' ', ' ', ' '}};
printf(isWonRow('X', game, 1) ? "true\n" : "false\n"); 
const char gg[3][3] = {{'X', 'O', ' '},{' ', ' ', ' '}, {'X', 'X', 'O'}};
printf(isWonRow('X', gg, 2) ? "true\n" : "false\n"); 
}