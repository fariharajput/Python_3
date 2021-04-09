# You need to implement the following functions in this file
# add_msg
# indexing
# search


class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0
    
    def get_total_words(self):
        return self.total_words
    
    def get_msg_size(self):
        return self.total_msgs
    
    def get_msg(self, n):
        return self.msgs[n]

    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs += 1
        return 
    
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        self.index[l] = m
        return

    # implement: query interface
    '''
    return a list of tupple. if index the first sonnet (p1.txt), then
    call this function with term 'thy' will return the following:
    [(7, "Feed'st thy light's flame with self-substantial fuel,"),
     (9, "Thy self thy foe, to thy sweet self too cruel:,"),
     (9, "Thy self thy foe, to thy sweet self too cruel:,"),
     (12, "Within thine own bud buriest thy content,")]
    '''

    def search(self, term):
        msgs = []

        for key, val in self.index.items():
            if term in val:
                msgs.append((key, val))

        return msgs


#main progrma
if __name__ == "__main__":
    my_idx = Index('test')
    my_idx.add_msg_and_index("who is this thing called")
    my_idx.add_msg_and_index("who knows who")
    search = my_idx.search('who')

    print("result is ",search)

    print('\n---------------')
    print("name: ",my_idx.name)
    print("msgs: ",my_idx.msgs)
    print("index: ",my_idx.index)
    print("total_msgs: ",my_idx.total_msgs)
    print("total_words: ",my_idx.total_words)
            