import contextlib, sys
import huffmancoding


def main():

	
	inputfile = '/home/tanmay/github/ASCII-program/Output.txt'
	outputfile = '/home/tanmay/github/ASCII-program/A Compressed Folder/NewOutput'


	freqs = get_frequencies(inputfile)
	freqs.increment(256)  
	code = freqs.build_code_tree()
	canoncode = huffmancoding.CanonicalCode(tree=code, symbollimit=freqs.get_symbol_limit())

	code = canoncode.to_code_tree()
	

	with open(inputfile, "rb") as inp, \
			contextlib.closing(huffmancoding.BitOutputStream(open(outputfile, "wb"))) as bitout:
		write_code_len_table(bitout, canoncode)
		compress(code, inp, bitout)



def get_frequencies(filepath):
	freqs = huffmancoding.FrequencyTable([0] * 257)
	with open(filepath, "rb") as input:
		while True:
			b = input.read(1)
			if len(b) == 0:
				break
			freqs.increment(b[0])
	return freqs


def write_code_len_table(bitout, canoncode):
	for i in range(canoncode.get_symbol_limit()):
		val = canoncode.get_code_length(i)

		if val >= 256:
			raise ValueError("The code for a symbol is too long")
		

		for j in reversed(range(8)):
			bitout.write((val >> j) & 1)


def compress(code, inp, bitout):
	enc = huffmancoding.HuffmanEncoder(bitout)
	enc.codetree = code
	while True:
		b = inp.read(1)
		if len(b) == 0:
			break
		enc.write(b[0])
	enc.write(256)  # EOF


if __name__ == "__main__":
	main()
