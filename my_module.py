'''
in this file we can create some user defined functions,variables,classes..
'''
def greet(name):
    """user defined function"""
    return (f'Hello {name}')
greet("Codegnan")

names = {'students':['sai','akash','ajay'],
        'age':[14,25,35]}
if __name__=="__main__":
    print(__name__)
    
def display():
    """subjects covered"""
    yield "Python"
    yield "GENAI"
    yield "RAG"
    yield "Agents"
print(display())
print(type(display()))
