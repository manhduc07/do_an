# Node class
class Node:

    # Hàm khởi tạo đối tượng 
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # tiếp theo


class LinkedList:

    def __init__(self):
        self.head = None