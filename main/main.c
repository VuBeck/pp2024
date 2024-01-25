#include<unistd.h>
#include<stdio.h>

int main(){
    printf("Main before fork()\n");
    int pid = fork();
    printf("Main after fork()\n");
    if(pid ==0) printf("pid is zero, value is %d\n",pid);
    else printf("pid is NOt zero, value is %d\n", pid);

    return 0;

}