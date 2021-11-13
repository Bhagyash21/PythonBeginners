class Dog:
    #variable
    eyes = 2
    fur = "soft"
    #function
    def __init__(self):
        print("This is automatically called. It is kind of constructor")
    def barks(self):
        print("Dog barks!")
    def play(self):
        print("Dog plays with ball and he is {}!".format(self.fur))


ginger = Dog()
ginger.play()
ginger.barks()
milo = Dog()
milo.play()
milo.barks()

#Below is another program which highlights use of self keyword.
# class Dog:
#     def __init__(self, breed, color):
#         eye = 2
#         self.color = color
#         self.breed = breed
#
#     def display_breed(self):
#         print(f"Name of your dog is {self.breed}")
#
#     def display_color(self):
#         print(f"Color of your dog is {self.color}")
#
#     def display_eye(self):
#         print(eye)
#
# dog1 = Dog("Husky", "Black")
# dog1.display_breed()
# dog1.display_color()
# dog1.display_eye()

