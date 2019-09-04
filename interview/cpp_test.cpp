//*.h

#include <iostream>
#include <string>
// using namespace std;

class Score
{
    float c_program;
    float Data_structure;
    float Math;

public:
    Score();
    Score(float c_program, float Data_structure, float Math);

    float average();
    void print_score();
    void Set_score(float c_program, float Data_structure, float Math);
};

enum SEX_TYPE
{
    FEMALE = 0,
    MALE = 1
};

class Student
{
public:
    std::string name;
    SEX_TYPE sex;
    Score myScore;

    Student();
    Student(std::string &name, SEX_TYPE sex, Score &myScore);
    float average();
    void Print_Info();
    void Set_Info(std::string &name, SEX_TYPE sex, Score &myScore);
};

//*.cpp

float Score::average()
{
    return (c_program + Data_structure + Math) / 3.0f;
}

void Score::print_score()
{
    fprintf(stdout, "C Program: %.2f,  Data Structure: %.2f,  Math: %.2f\n", c_program, Data_structure, Math);
}

void Score::Set_score(float c_program, float Data_structure, float Math)
{
    this->c_program = c_program;
    this->Data_structure = Data_structure;
    this->Math = Math;
}

Score::Score()
{
    Set_score(0, 0, 0);
}
Score::Score(float c_program, float Data_structure, float Math)
{
    Set_score(c_program, Data_structure, Math);
}

float Student::average()
{
    return myScore.average();
}

const char *sex_strs[2];

void Student::Print_Info()
{
    fprintf(stdout, "Name:  %s, Sex:  %s,  ", name.c_str(), sex_strs[sex]);
    myScore.print_score();
}
void Student::Set_Info(std::string &name, SEX_TYPE sex, Score &myScore)
{
    this->name = name;
    this->sex = sex;
    this->myScore = myScore;
}

Student::Student()
{
    std::string name = std::string("No Name");
    Score score = Score();
    Set_Info(name, SEX_TYPE::FEMALE, score);
}
Student::Student(std::string &name, SEX_TYPE sex, Score &myScore)
{
    Set_Info(name, sex, myScore);
}

#define STUDENT_COUNT 1000

int main()
{
    sex_strs[FEMALE] = "FEMALE";
    sex_strs[MALE] = "MALE";
    Student student[STUDENT_COUNT];
    for (int i = 0; i < STUDENT_COUNT; i++)
    {
        std::string name = std::string("No Name");
        Score score = Score();
        student[i] = Student(name, SEX_TYPE::FEMALE, score);
    }

    for (int i = 0; i < STUDENT_COUNT; i++)
    {
        student[i].Print_Info();
    }
    return 0;
}