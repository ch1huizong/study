// T: 读写二进制文件
// fopen, fclose, ftell, fseek, fwrite, fread, sprintf

#include <stdio.h>
#include <stdlib.h>

const int STR_LEN = 20;

typedef struct _student {
    char name[20];
    int gender;
    int age;
} Student;

void getList(Student aStu[], int number);
int save(Student aStu[], int number);
void read(FILE *fp, int index);

int main(int argc, char *argv[]) {
    int number = 0;
    printf("输入学生数量: ");
    scanf("%d", &number);
    Student aStu[number];

    getList(aStu, number);
    if (save(aStu, number)) {
        printf("保存成功\n");
    } else {
        printf("保存失败\n");
    }

    // 数据随机读写
    FILE *fp = fopen("student.data", "r");
    if (fp) {
        fseek(fp, 0L, SEEK_END);
        long size = ftell(fp);
        int number = size / sizeof(Student); // 有多少个条目?
        int index = 0;

        printf("你有%d个数据，你要看第几个: ", number);
        scanf("%d", &index);
        read(fp, index - 1);
        fclose(fp);
    }

    return 0;
}

void getList(Student aStu[], int number) {
    char format[STR_LEN];
    sprintf(format, "%%%ds", STR_LEN - 1);  // 产生format字符串

    for (int i = 0; i < number; ++i) {  // 注意数组越界
        printf("第%d个学生:\n", i + 1);
        printf("\t姓名: ");
        scanf(format, aStu[i].name);  // 数组名可以表示地址 
        printf("\t性别 (0-男, 1-女, 2-其他): ");
        scanf("%d", &aStu[i].gender);
        printf("\t年龄: ");
        scanf("%d", &aStu[i].age);
    }
}

int save(Student aStu[], int number) {
    int ret = -1;
    FILE *fp = fopen("student.data", "w");
    if (fp) {
        ret = fwrite(aStu, sizeof(Student), number, fp);  // aStu内存指针
        fclose(fp);
    }

    return ret == number;
}

void read(FILE *fp, int index) {
    fseek(fp, index * sizeof(Student), SEEK_SET);  // 文件指针移位
    Student stu;

    if (fread(&stu, sizeof(Student), 1, fp) == 1) {
        printf("第%d个学生: \n", index + 1);
        printf("\t姓名: %s\n", stu.name);
        printf("\t性别: ");
        switch (stu.gender) {
            case 0:
                printf("男\n");
                break;
            case 1:
                printf("女\n");
                break;
            case 2:
                printf("其他\n");
                break;
        }
        printf("\t年龄: %d\n", stu.age);
    }
}
