"""
Needleman–Wunsch algorithm for global sequence alignment (starting template)

Your task is to complete the implementation of the Needleman-Wunsch algorithm
for global sequence alignment. The algorithm should take two DNA sequences
and align them using dynamic programming.

Scoring scheme:
- Match: +1
- Mismatch: -1
- Gap: -2
"""

def needleman_wunsch(seq1, seq2, match, mismatch, gap):
    ''' Perform global alignment between seq1 and seq2 using the Needleman-Wunsch algorithm '''
    n, m = len(seq1), len(seq2)

    # Initializing the DP matrix with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    traceback = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

    # TO-DO: Initialize first row and first column with gap penalties

    # TO-DO: Fill in the DP matrix
    # For each cell (i, j), compute:
    #   diag = dp[i-1][j-1] + (match/mismatch)
    #   up   = dp[i-1][j] + gap
    #   left = dp[i][j-1] + gap
    # max(diag, up, left) of dp[i][j] 


    return dp, traceback


def traceback_alignment(traceback, seq1, seq2):
    ''' Perform traceback to recover at least one optimal alignment '''

    i, j = len(seq1), len(seq2)
    aligned1, aligned2 = "", ""

    # TO-DO: Traceback from bottom-right (i,j) to (0,0).
    #   If diag, take characters from both sequences.
    #   If top, take character from seq1 and gap in seq2.
    #   If left, take from seq2 and gap in seq1.

    return aligned1[::-1], aligned2[::-1]  # reverse at the end


def print_matrix(dp, seq1, seq2):
    ''' Print the DP matrix '''
    header = "      " + "   ".join("-" + seq2)
    print(header)
    for i in range(len(seq1)+1):
        row_label = "-" if i == 0 else seq1[i-1]
        row = [f"{dp[i][j]:3d}" for j in range(len(seq2)+1)]
        print(f"{row_label}  " + "  ".join(row))


if __name__ == "__main__":
    # Test Case 1
    seq1 = "TCCA"
    seq2 = "TCGCA"

    dp, tb = needleman_wunsch(seq1, seq2)
    print("DP Matrix:")
    print_matrix(dp, seq1, seq2)

    aligned1, aligned2 = traceback_alignment(tb, seq1, seq2)
    print("\nOptimal Alignment:")
    print(aligned1)
    print(aligned2)
    print("score:", dp[len(seq1)][len(seq2)])
