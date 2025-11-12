course = "Python's course for Beginners"
print(course)

course = 'Python course for "Beginners"'
print(course)

course = ''' 
Hi John,

here is our first email to you

Thank you
'''
print(course)

course = 'Python for beginners'
another = course[:]
print(course[0])
print(course[-1])
print(course[-2])

print(course[0:3])

print(course[0:])

print(course[3:5])

print(course[:4])

print(course[:])

print(another)

name = "Jennifer"
print(name[1:-1])


first = "John"
last = "Smith"

message = first + " [" + last + "] is a coder" 
print(message)

msg = f"{first} [{last}] is a coder]" #formatted string. schoener. Variablen in geschweifte Klammern
print(msg)

course = "Python for Beginners"
print(len(course)) #Laenge von verschiedenen Sachen. Auch laenge von listen

print(course.upper()) #GROSS schreiben des strings.
print(course)           # Aber der alte String wird nicht veraendert und ist immernoch klein!
print(course.lower()) #oder klein
print(course.title()) #Anfang gross

print(course.find("P")) #"P" ist das erste mal an Position 0
print(course.find("o")) #"o" ist das erste mal an Position 4

print(course.find("O")) #"O"  (grosses O) ist nirgends, also -1
print(course.find("Beginners")) #"Beginners" startet bei Position 11

print(course.replace("Beginners", "Absolute Beginners")) # Text ersetzen
print(course)#der ehemalige String wird aber wieder NICHT veraendert
print(course.replace("P", "J")) # Text ersetzen

print("Python" in course) #Bool. Abfrage ob in variable enthalten

