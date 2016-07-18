"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   ENCAPSULATION: One of the advantages of object orientation is that
   you can group together data and any methods and behaviors that
   closely relate to or tie into that data so that they stay close
   together.

   ABSTRACTION: Another advantage of object orientation is that you
   can hide the finer details of how something works, so that you
   do not have to see and work with those finer details all the time.

   POLYMORPHISM: A third advantage of object orientation is the
   flexibility to use the same method in different places and add
   slight variations to it. Thus, when the method is called, it is
   called in the same way, but in reality, a variation of the method
   is being implemented.


2. What is a class?

   A class is an object used to encapsulate data, methods, and
   behaviors, add a level of abstracton if needed, and can be
   used to hold methods that can be used in a polymorphic way.


3. What is an instance attribute?

   An instance attribute is data/characteristics that is given to each
   instance of a class. Thus, these attributes are assigned each time
   when a class is instantiated.


4. What is a method?

   A method is a like a function but it lives within a class. Methods
   define in which way you can interact with a class.


5. What is an instance in object orientation?

   An instance is a specific occurrence of a class.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is data/characteristics that is given to the
   class, so every instance of the class will have that attribute.
   However, an instance attribute is only applied to each instance of
   the class.

   For example, if you had a class called Shapes that encompassed
   many different shapes and their commonality was that they all
   had lines, lines = True may be a class attribute. A specific
   occurrence of Shapes is an instance, so a "Circle", a "Square",
   and a "Trapezoid" may be some instances. If those were their
   names, then name = "Circle" or name = "Square" are instance
   attributes. Another instance attribute can be their line type,
   such as for "Circle", line_type = "curved".

"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

        return (self.question, self.correct_answer)

    def ask_and_evaluate(self):
        print self.question
        user_answer = raw_input(">>>   ")
        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        exam_question = Question(question, correct_answer)
        self.question.append(exam_question)

    def administer(self):
        score = 0

        for question in self.questions:
            new_question = Question(question[0], question[1])
            result = new_question.ask_and_evaluate()
            if result == True:
                score += 1

        return score



def take_test(exam, student):
    new_exam = Exam(exam)
    score = new_exam.administer()


def example():
    exam_example = Exam("Example")

    exam_example.add_question("What is 10 + 15?", 25)
    exam_example.add_question("What is 60 / 10?", 6)
    exam_example.add_question("What is x * 1?", "x")

    student_example = Student("Jane", "Doe", "123 Here")

    take_test(exam_example, student_example)


class Quiz(Exam):
    def administer(self):
        results = super(Quiz, self).administer()

        if results >= (total_questions / 2):
            return True
        else:
            return False
















