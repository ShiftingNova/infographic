from graphics import graphics
def main():
    file_name =input("enter file name")
    file = open(file_name,'r')
    gui = graphics(500,500, "Infographic")
    text = []
    list = []
    unique = []
    small = 0
    medium = 0
    large = 0
    cap = 0
    no_cap = 0
    for i in file:
        text.append(i.split(" "))
    for i in text:
        for e in i:
            list.append(e.replace(".\n",""))
    print(list)
    for i in list:
        if i not in unique:
            unique.append(i.replace("\n",""))
    print(unique)

    for i in unique:
        if len(i) <= 4:
            small += 1
        elif len(i) <= 7:
            medium += 1
        else:
            large += 1
    for i in list:
        if i[0]==i[0].upper():
            cap+=1
        else:
            no_cap+=1
    words_count = {}
    for i in unique:
        value = 0
        for e in list:
            if i==e:
                value += 1
        words_count[i] = value
    print(words_count)
    pop_key = ""
    pop_value = 0
    for key in words_count:
        if words_count[key] > pop_value:
            pop_key = key
            pop_value = words_count[key]
    unique_count = len(unique)
    count =(450/unique_count)*small
    second_count = count + ((450/unique_count)*medium)
    total = cap+no_cap
    cap_count = (450/total)*cap
    while True:
        gui.rectangle(0, 0, 500, 500, 'gray')
        gui.text(10,0,'text.txt','light blue')
        gui.text(10,25,'unique\nwords:'+str(unique_count),'white')
        gui.text(10,75,"popular\nwords:\n"+pop_key+" "+str(pop_value),'white')
        gui.text(100,2,"word lengths",'white')
        gui.rectangle(100,25,100,count,'blue')
        gui.text(100,25,'small words','white',10)
        gui.rectangle(100, 25+count, 100, (450/unique_count)*medium, 'green')
        gui.text(100, 25+count, 'medium words', 'white', 10)
        gui.rectangle(100, 25 + second_count, 100, (450/unique_count)*large, 'red')
        gui.text(100, 25 + second_count, 'large words', 'white', 10)
        gui.text(300, 2, "cap/noncap", 'white')
        gui.rectangle(300,25,100,(450/total)*cap,'blue')
        gui.text(300,25,'Cap','white',10)
        gui.rectangle(300,25+cap_count,100,(450/total)*no_cap,'green')
        gui.text(300,25+cap_count,'No Cap','white',10)
        gui.update_frame(60)

    gui.primary.mainloop()
main()
