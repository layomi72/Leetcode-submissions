class Node{
    public:
        int value;
        Node* next;
        Node* prev;
        Node(int value){
            this->value = value;
            this->next = nullptr;
            this->prev = nullptr;
        }
};

class Deque {
public:
    Node* head;
    Node* tail;
    Deque() {
        this->head = new Node(-1);
        this->tail = new Node(-1);
        this->head->next = tail;
        this->tail->prev = head;

    }

    bool isEmpty() {
        if (this->head->next == this->tail){
            return true;
        }
        else{
            return false;
        }
            
    }

    void append(int value) {
        Node* new_node = new Node(value);
        Node* last_node = this->tail->prev;

        last_node->next = new_node;
        new_node->prev = last_node;
        new_node->next = this->tail;
        this->tail->prev = new_node;
        
    }

    void appendleft(int value) {
        Node* new_node = new Node(value);
        Node* first_node = this->head->next;

        this->head->next = new_node;
        new_node->prev = this->head;
        new_node->next = first_node;
        first_node->prev = new_node;
    }

    int pop() {
        if (this->isEmpty()){
            return -1;
        }
        Node* last_node = this->tail->prev;
        int value = last_node->value;
        Node* prev_node = last_node->prev;

        prev_node->next = this->tail;
        this->tail->prev = prev_node;

        return value;
    }

    int popleft() {
        if (this->isEmpty()){
            return -1;
        }
        Node* first_node = this->head->next;
        int value = first_node->value;
        Node* next_node = first_node->next;

        this->head->next = next_node;
        next_node->prev = this->head;

        return value;

    }
};
