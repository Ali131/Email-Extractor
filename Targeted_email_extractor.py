 #email:	king.ali.1331@gmail.com
 #!/usr/bin/python

def banner():
	print '====================================================='
	print '|!!|	     	Target Email extractor		|!!|'
	print '====================================================='

banner()
	
inpt=raw_input('Input file name e.g. input.txt: ')
oupt=raw_input('Output file name e.g. output.txt: ')
emails=raw_input('Type of emails you wanna extract e.g. @gmail.com: ') 
	
if __name__ == '__main__':
	f = open(oupt,'w+')
	print 'Please Wait. File in Process.....'
	ff = open(inpt, 'r+')
	for lines in ff:
		if emails in lines:
			print 'Email Found!'
			f.write(lines)
	ff.close()
	f.close()
	
print '.../done'
