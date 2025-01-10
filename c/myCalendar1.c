struct event { 
    int start;
    int end;
    struct event *next;
};

typedef struct {
    struct event *head;
} MyCalendar;


MyCalendar* myCalendarCreate() {
    MyCalendar* calendar = (MyCalendar*)malloc(sizeof(MyCalendar));
    calendar->head = NULL;
    return calendar;
}

bool myCalendarBook(MyCalendar* obj, int start, int end) {
    struct event *temp = obj->head;
    struct event *prev = NULL;

    while (temp) {
        bool overlap1 = (start < temp->end) && (end > temp->start);
        if (overlap1) {
            return false;
        }
        prev = temp;
        temp = temp->next;
    }

    struct event *newEvent = (struct event*)malloc(sizeof(struct event));
    newEvent->start = start;
    newEvent->end = end;
    newEvent->next = NULL; 

    if (prev == NULL) {
        obj->head = newEvent;
    } else {
        prev->next = newEvent;
    }

    return true;
}

void myCalendarFree(MyCalendar* obj) {
    struct event *temp = obj->head;
    while (temp != NULL) {
        struct event *temp2 = temp;
        temp = temp->next;
        free(temp2);
    }
    free(obj);
}

/**
 * Your MyCalendar struct will be instantiated and called as such:
 * MyCalendar* obj = myCalendarCreate();
 * bool param_1 = myCalendarBook(obj, start, end);
 * myCalendarFree(obj);
 */


