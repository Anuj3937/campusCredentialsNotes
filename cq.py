class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued: {removed}")
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print(f"Front element: {self.queue[self.front]}")
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue contents:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()
def main():
    size = int(input("Enter the capacity of Circular Queue: "))
    cq = CircularQueue(size)
    while True:
        print("\n-Circular Queue Menu")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter element to enqueue: ")
            cq.enqueue(item)
        elif choice == "2":
            cq.dequeue()
        elif choice == "3":
            cq.peek()
        elif choice == "4":
            cq.display()
        elif choice == "5":
            print("exiting program")
            break
        else:
            print("invalid choice ")
if __name__ == "__main__":
    main()