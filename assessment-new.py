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

   A class is a data structure to hold data, methods, and behaviors
   about the class. This information is then initialized when the
   class is instantiated.


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


class Student(object):
    """Student data - first name, last name, address."""
    def __init__(self, first_name, last_name, address):
        """Instantiates Student with first name, last name, and address."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Question and answer data as well as an evaluation method."""
    def __init__(self, question, correct_answer):
        """Instantiates Question with a question and a correct answer."""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Method for Question to compare user-input answer with the correct answer"""
        print self.question
        answer = raw_input(">>>   ")

        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Exam that holds list of questions and methods."""
    def __init__(self, name):
        """Instantiates Exam with an exam name."""
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Exam method to add questions and answers to the list of questions."""
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Exam method to administer the exam and return a score."""
        score = 0

        for exam_question in self.questions:
            if exam_question.ask_and_evaluate() is True:
                score += 1

        return score


def take_test(exam, student):
    """Function to administer an Exam, add score instance attribute for Student."""
    score = exam.administer()
    student.score = score

    if student.score is True:
        print "Congratulations! You have passed!"
    elif student.score is False:
        print "Sorry. You have failed."
    else:
        print "Test Score: {} out of {} correct".format(student.score, len(exam.questions))


class Quiz(Exam):
    """Class that holds Quiz data, which inherits from Exam."""
    def administer(self):
        """To override Exam's administer method to return True/False instead of score."""
        if super(Quiz, self).administer() >= (len(self.questions)/2):
            return True
        else:
            return False


def example():
    """Function to test Exam class."""
    sample_exam = Exam("Sample")
    sample_student = Student("Jane", "Doe", "101 Here")

    sample_exam.add_question("What is x?", "x")
    sample_exam.add_question("What is y?", "y")
    sample_exam.add_question("What is z?", "z")

    take_test(sample_exam, sample_student)


def example_quiz():
    """Function to test Quiz class."""
    sample_quiz = Quiz("Example")
    example_student = Student("John", "Doe", "102 There")

    sample_quiz.add_question("What is A?", "A")
    sample_quiz.add_question("What is B?", "B")
    sample_quiz.add_question("What is C?", "C")

    take_test(sample_quiz, example_student)
