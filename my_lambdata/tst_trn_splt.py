import pandas


def train_test_split(split):
    """
    Create a pandas dataframe

    Split data into train, val, test function

    Train/test 80/20
    """
    return split

if __name__ == "__main__":

    df = pandas.DataFrame({
        'a':[11, 42, 26, 9, 29],
        'b':[21, 32, 2, 14, 19],
        'c':[27, 29, 18, 34, 14], 
        'd':[31, 18, 3, 11, 13],
        'e':[41, 15, 36, 7, 20]}
    )

    train = df[df['a'], + df['b'], + df['c']]
    test = df['e', 'd']

    print(train)
    print(test)