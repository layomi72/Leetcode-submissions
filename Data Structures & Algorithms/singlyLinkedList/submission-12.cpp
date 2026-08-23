class Node {
    public:
        int value;
        Node* next;
        Node(int value){
            this->value = value;
            next = nullptr;
        }
};


class LinkedList {
private:
    Node* head;
    Node* tail;
public:
    LinkedList() {
        head = new Node(-1);
        tail = head;
    }

    int get(int index) {
        Node* current = head->next;
        int i = 0;
        while (i < index && current != nullptr){
            current = current->next;
            i +=1;
        }
        if(current == nullptr){
            return -1;
        }
        else{
            return current->value;
        }

    }

    void insertHead(int val) {
        Node* value2insert = new Node(val);

        if (head->next != nullptr){
            Node* current = head->next;
            head->next = value2insert;
            value2insert->next = current;
        }
        else{
            head->next = value2insert;
            tail = value2insert;
        }
    }
    
    void insertTail(int val) {
       tail->next = new Node(val);
       tail = tail->next;
    }

    bool remove(int index) {
        int i = 0;
        Node*  current = head;
        while(i < index && current != nullptr){
            i += 1;
            current = current->next;
        }
        if (current == nullptr || current->next == nullptr){
            return false;
        }
        else {
            if (current->next == tail) {
                tail = current;
            }
            current->next = current->next->next;
            return true;
        }
        
    }

    vector<int> getValues() {
        vector<int> answer;
        Node* current = head->next;
        while(current != nullptr){
            answer.push_back(current->value);
            current = current->next;
        }
        return answer;
        
    }
};