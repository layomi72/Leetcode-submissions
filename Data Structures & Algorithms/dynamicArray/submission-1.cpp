class DynamicArray {
private:
    int length;
    int capacity;
    int* listt;
    int* new_listt;
public:
   

    DynamicArray(int capacity) {
        listt = new int[capacity];
        this->length = 0;
        this->capacity = capacity;
    }

    int get(int i) {
        return listt[i];
    }

    void set(int i, int n) {
        listt[i] = n;
    }

    void pushback(int n) {
        if(length == capacity){
            resize();
        }
        listt[length] = n;
        length++;
    }

    int popback() {
        length--;
        return listt[length];
    }

    void resize() {
        capacity = 2 * capacity;
        new_listt = new int[capacity];
        for (int i = 0; i < length; i++){
            new_listt[i] = listt[i];
        }
        listt = new_listt;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
