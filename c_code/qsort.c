#include<stdio.h>

void qsort(int v[], int left, int right) {
    if (left >= right)
        return ;

    int i, ind;
    void swap(int v[], int left, int right);
    ind = left;
    for(i = left + 1; i <= right; i ++){
        if(v[i] < v[left])
            swap(v, ++ind, i);
    }
    swap(v, left, ind);
    qsort(v, left, ind - 1);
    qsort(v, ind + 1, right);
}

void swap(int v[], int left, int right){
    int temp;
    temp = v[right];
    v[right] = v[left];
    v[left] = temp;
}

void main() {
    int v[] = {8,7,3,1,4,5,6,9};
    qsort(v, 0, 7);
    for(int i=0; i < 8; i++)
        printf("v[%d]:%d\n", i, v[i]);
}
