#include <iostream>
using namespace std;

const int MAX = 5;

int* bubbleSort(int* array);
void showArray(int* array);

int main() {
    int* array = new int[MAX];

    for (int i = 0; i < MAX; i++) {
        cout << "Informe o " << i + 1 << "º inteiro: ";
        cin >> array[i];
    }

    cout << "Vetor informado: "; 
    showArray(array);
    
    int* sorted_array = bubbleSort(array);

    cout << "Vetor ordenado: ";
    showArray(sorted_array);
}

int* bubbleSort(int* array) {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    return array;
}

void showArray(int* array) {
    cout << "[";
    for (int i = 0; i < MAX - 1; i++) {
        cout << array[i] << ", ";
    }
    cout << array[MAX - 1] << "]\n";
}