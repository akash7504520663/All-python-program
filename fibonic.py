class FibSeq:
    def __init__(self):
        self.Fs1 = 1
        self.Fs2 = 0
    def next_seq(self):
        a=  self.Fs1
        b = self.Fs2
        c=a+b 
        self.Fs2 = self.Fs1
        self.Fs1 = c
        return c
        
newFib = FibSeq()
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())
print(newFib.next_seq())

