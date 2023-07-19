import csv

class Node:
    __slots__ = ['achievement', 'next']

    def __init__(self, achievement):
        self.achievement = achievement
        self.next = None
        
class LinkedStack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, achievement):
        new_node = Node(achievement)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        node = self.top
        self.top = self.top.next
        return node

    def peek(self):
        if self.is_empty():
            return None
        return self.top

    def CSV(self,file_name):

        # Create a CSV file for each student's achievements
        achievements = []

        while not self.is_empty():
            student_achievement = self.pop().achievement
            achievements.append(student_achievement)

            # Write the achievements to a CSV file
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(achievements)