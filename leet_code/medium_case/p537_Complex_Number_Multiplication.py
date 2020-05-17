class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        # display complex as a list t, t[0] is the real, t[1] is imaginary
        """
        (at[0] + at[1]*i) * (bt[0] + bt[1]*i) 
        = at[0]*bt[0] + at[0]*bt[1]*i + at[1]*i*bt[0] - at[1]*bt[1]
        = at[0]*bt[0] - at[1]*bt[1] + (at[0]*bt[1] + at[1]*bt[0]) * i
        """
        
        at = [int(i) for i in a[:-1].split('+')]
        bt = [int(i) for i in b[:-1].split('+')]
        
        return "{0}+{1}i".format(at[0]*bt[0] - at[1]*bt[1], at[0]*bt[1] + at[1]*bt[0])
