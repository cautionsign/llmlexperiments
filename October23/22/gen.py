# Create a file named 'opera_game.pgn' and paste the PGN of the Opera Game into it.
# Save the file and close it.
pgn_content = """
[Event "Opera game"]
[Site "Paris, France"]
[Date "1858.??.??"]
[EventDate "?"]
[Round "?"]
[Result "0-1"]
[White "Paul Morphy"]
[Black "Duke Karl / Count Isouard"]
[ECO "C41"]
[WhiteElo "?"]
[BlackElo "?"]
[PlyCount "42"]

1.e4 e5 2.Nf3 d6 3.d4 Bg4 4.dxe5 Bxf3 5.Qxf3 dxe5 6.Bc4 Nf6 7.Qb3 Qe7 8.Nc3 c6
9.Bg5 b5 10.Nxb5 cxb5 11.Bxb5+ Nbd7 12.O-O-O Rd8 13.Rxd7 Rxd7 14.Rd1 Qe6 15.Bxd7+
Nxd7 16.Qb8+ Nxb8 17.Rd8# 0-1
"""

with open("opera_game.pgn", "w") as pgn_file:
    pgn_file.write(pgn_content)

print("Opera Game PGN has been manually saved as 'opera_game.pgn'.")

