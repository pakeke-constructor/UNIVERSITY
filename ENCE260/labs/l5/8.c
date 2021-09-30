


#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define u32 uint32_t
#define u16 uint16_t
#define u8  uint8_t

#define i32 int32_t
#define i16 int16_t
#define i8  int8_t



#define MAX_FNAME 80

size_t readString(char* string, size_t max)
{
    size_t i = 0;
    int c;
    while ((c = getchar()) != EOF && c != '\n' && i < max) {
        string[i] = c;
        i++;
    }
    string[i] = '\0';
    return i;
}



const char *parseline(char* str, u32 len)
{
    str[0] = toupper(str[0]);
    bool last_space = false;
    for (u32 i=1; i < len; i++) {
        if (last_space) {
            str[i] = toupper(str[i]);
            last_space = false;
        } else {
            str[i] = tolower(str[i]);
        }

        if (isspace(str[i])) {
            last_space = true;
        }
    }
    return str;
}


FILE* openInputFile(char *fname)
{
    FILE *handle;
    handle = fopen(fname, "r");
    if (!handle) {
        printf("Input file can't be opened\n");
        return NULL;
    } else {
        return handle;
    }
}



FILE* openOutputFile(char *fname)
{
    FILE *handle;
    handle = fopen(fname, "w+");
    if (!handle) {
        printf("Output file can't be opened\n");
        return NULL;
    } else {
        return handle;
    }
}



int main()
{
    char inputf[MAX_FNAME + 1];
    char outputf[MAX_FNAME + 1]; // account for \0 char.

    readString(inputf, MAX_FNAME);
    readString(outputf, MAX_FNAME);

    FILE *infile = openInputFile(inputf);
    FILE *outfile = openOutputFile(outputf);
    
    if (!outfile || !infile) {
        if (outfile) {
            fclose(outfile);
        }
        if (infile) {
            fclose(infile);
        }
        return 1;
    }

    int max_size = 10000;
    char buffer[max_size]; // Assume max line size is 10000 chars
    
    while (fgets(buffer, max_size, infile)) {
        parseline(buffer, strlen(buffer));
        fprintf(outfile, "%s", (char*)buffer);
    }

    fclose(infile);
    fclose(outfile);
}




