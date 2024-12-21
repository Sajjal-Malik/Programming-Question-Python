from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def size(self):
        pass

class File(Component):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def size(self):
        return self.__size
    
class Folder(Component):
    def __init__(self, name, components):
        self.__name = name
        self.__components = components
    
    def size(self):
        total = 0
        for component in self.__components:
            total += component.size()
        return total
    
    def add(self, component):
        self.__components.append(Component)

resume = File("resume.doc", 1024)
cover_letter = File("cover_letter.doc", 2048)
refenerce = File("refenerce.pdf", 4096)

documents = Folder("Documents", [resume, cover_letter, refenerce])

todo = File("todo.txt", 256)
screenshot = File("screenshot.png", 25000)

desktop = Folder("Desktop", [todo, screenshot])

user = Folder("User", [desktop, documents])

# new_file = File("secret.txt", 256)

# user.add(new_file)

print(resume.size())
print(documents.size())
print(desktop.size())
print(user.size())

components = [todo, resume, cover_letter, refenerce, screenshot]

for comp in components:
    print(comp.size())