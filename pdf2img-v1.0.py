from pdf2image import convert_from_path
a = 'y'
print('***Write PDF file name with full directory if it is not in the same directory of this application')
print('***write only file name name if both are in same folder')
print('***Image will be downloaded in the same directory of the application, not PDF')
while a == 'y' or a == 'Y':
    images = convert_from_path(input("PDF file name: "))
    for i in range(len(images)):
        images[i].save('page'+str(i)+'.jpg','JPEG')
    a = input('do you want to convirt another? y/n\n')
input('press any key to exit')
