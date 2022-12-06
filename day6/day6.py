def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input_list = f.readlines()

    return input_list


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst)-3):
        yield lst[i:i + n]


def get_answer(input, chunksize):
    i = 0
    for chunk in chunks(input[0], chunksize):

        if len(set(chunk)) == chunksize:
            print(i+chunksize, chunk)
            break
        i += 1


input = read_input('input.txt')
get_answer(input, 4)
get_answer(input, 14)