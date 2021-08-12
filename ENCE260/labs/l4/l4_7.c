

#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

typedef struct {
    uint32_t id;
    uint8_t age;
    float gpa;
} Student_t;


Student_t newStudent(uint64_t id, uint8_t age, float gpa)
{
    return (Student_t) {
        id, age, gpa
    };
}


void printStudent(const Student_t* student)
{
    printf("%d: Age %d, GPA %.2f\n", student->id, student->age, student->gpa);
}

void updateGpa(Student_t* student, float newGpa)
{
    student->gpa = newGpa;
}



int main(){
    Student_t student = newStudent(12345678, 19, 5.62);
printStudent(&student);
updateGpa(&student, 6.2);
printStudent(&student);
}

