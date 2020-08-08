def generateTemplate(numPlayers):
    """Generates html text for player name selection forms
    """
    template = """<section>
						<label for="player%d">Player %d's Name</label>
							<input type="text" name="player%d" value="Player %d">
					</section>"""

    out = ""

    for ii in range(numPlayers):
        out = out + (template % ii)

    return out