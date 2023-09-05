def is_repeat(seq):
    seq_len = len(seq)

    for repeat_len in range(1, int(seq_len/2)+1):
        if seq_len%repeat_len == 0:
            repeat_content = seq[0: repeat_len]
            number = int(seq_len/repeat_len)
            target = number*repeat_content

            if seq == target:
                return repeat_len

    return 0

seq1 = "AAAAAAAAAAAAAAAA"
seq2 = "CACACACACACACAC"
seq3 = "ATTCGATTCGATTCG"
seq4 = "GTAGTAGTAGTAGTA"
seq5 = "TCAGTCACTCACTCAG"

repeat_len = is_repeat(seq5)
if repeat_len != 0:
    seq_len = len(seq5)
    repeat_content = seq5[0: repeat_len]
    number = int(seq_len/repeat_len)
    print("The DNA sequence consists of", number, repeat_content)
else:
    print("The DNA sequence doesn't consist of a (integer) number of (perfect) tandem repeats")
