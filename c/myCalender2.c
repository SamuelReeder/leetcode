struct event { 
    int start;
    int end;
    struct event *next;
};

typedef struct {
    struct event *head;
} MyCalendarTwo;


MyCalendarTwo* myCalendarTwoCreate() {
    MyCalendarTwo* calendar = (MyCalendarTwo*)malloc(sizeof(MyCalendarTwo));
    calendar->head = NULL;
    return calendar;
}

bool myCalendarTwoBook(MyCalendarTwo* obj, int start, int end) {
    struct event *temp1 = obj->head;
    
    while (temp1) {
        if (start < temp1->end && end > temp1->start) {
            int overlap_start = fmax(start, temp1->start);  
            int overlap_end = fmin(end, temp1->end);        
            
            struct event *temp2 = obj->head;
            while (temp2) {
                if (temp2 != temp1 && overlap_start < temp2->end && overlap_end > temp2->start) {
                    return false;
                }
                temp2 = temp2->next;
            }
        }
        temp1 = temp1->next;
    }

    struct event *newEvent = (struct event*)malloc(sizeof(struct event));
    newEvent->start = start;
    newEvent->end = end;
    newEvent->next = NULL; 

    if (obj->head == NULL) {
        obj->head = newEvent;
    } else {
        struct event *temp = obj->head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = newEvent;
    }

    return true;
}

void myCalendarTwoFree(MyCalendarTwo* obj) {
    struct event *temp = obj->head;
    while (temp != NULL) {
        struct event *temp2 = temp;
        temp = temp->next;
        free(temp2);
    }
    free(obj);
}

/**
 * Your myCalendarTwo struct will be instantiated and called as such:
 * myCalendarTwo* obj = myCalendarTwoCreate();
 * bool param_1 = myCalendarTwoBook(obj, start, end);
 * myCalendarTwoFree(obj);
 */

