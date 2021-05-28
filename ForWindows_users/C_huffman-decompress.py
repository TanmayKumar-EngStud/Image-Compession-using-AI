import sys
import huffmancoding


def main():
	
	inputfile = 'C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\A Compressed Folder\\NewOutput'
	outputfile = 'C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\B Text Folder\\Result.txt'
	
	with open(inputfile, "rb") as inp, open(outputfile, "wb") as out:
		bitin = huffmancoding.BitInputStream(inp)
		canoncode = read_code_len_table(bitin)
		code = canoncode.to_code_tree()
		decompress(code, bitin, out)


def read_code_len_table(bitin):
	def read_int(n):
		result = 0
		for _ in range(n):
			result = (result << 1) | bitin.read_no_eof()  
		return result
	
	codelengths = [read_int(8) for _ in range(257)]
	return huffmancoding.CanonicalCode(codelengths=codelengths)


def decompress(code, bitin, out):
	dec = huffmancoding.HuffmanDecoder(bitin)
	dec.codetree = code
	while True:
		symbol = dec.read()
		if symbol == 256:  
			break
		out.write(bytes((symbol,)))


if __name__ == "__main__":
	main()
