input_data = open('input.txt', 'r') 
data = input_data.readlines()
a = int(data[0])
b = int(data[1])
if a<b:
    output_data = open('output.txt', 'w')
    output_data.write('<')
elif a>b:
    output_data = open('output.txt', 'w')
    output_data.write('>')
else:
    output_data = open('output.txt', 'w')
    output_data.write('=')
input_data.close()
output_data.close()