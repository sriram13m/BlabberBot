import re
out = open("KatyPerry.txt", "w")
with open("KatyperryTweets.txt") as file:
    for line in file:
        print(line)
        count = 0
        leng = len(line)
        for i in range(leng):
            if line[i] == "|":
                count +=1
            if(count == 2):
                if line[i+1] == 'R' and line[i+2] == 'T':
                    str = line[i+4:]
                elif line[i+1] == '@':
                    while line[i]!= ' ':
                        i+=1
                    str = line[i:]
                else:
                    str = line[i+1:]
                str = " ".join(filter(lambda str:str[0]!="@", str.split())) +"\n"
                str = re.sub(r'http\S+', '', str)
                out.write(str)
                break

    #print(data)
