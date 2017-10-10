text = 'Sample Text to Save ...\nNew line!!!'

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()
