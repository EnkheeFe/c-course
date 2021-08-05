from abc import ABC, abstractmethod, abstractproperty

class Node(ABC):
    def __init__(self, content, attributes):
        self.__children = []
        self.__attributes = attributes
        self.__content = content
    @property
    def content(self):
        return self.__content
    @property
    def children(self):
        return self.__children
    @abstractmethod
    def html(self):
        pass
    def appendChild(self, child):
        self.__children.append(child)

class Div(Node):
    def html(self):
        str = '<div>'
        str += self.content
        str += '</div>'
        return str
class B(Node):
    def html(self):
        str = '<b>'
        for child in self.children:
            str += child.html()
        str += self.content
        str += '</b>'
        return str

def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    #print(divA.html())
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = Div('This is a test B', divAtts)
    b = B('', {})
    b.appendChild(divB)
    print(b.html())
    
if __name__ == "__main__":
    main()
