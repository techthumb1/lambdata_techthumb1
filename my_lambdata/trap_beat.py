# trap_beat.py


class TrapBeat():

    '''Create a simple 4 bar beat.

    Params: Kick, snare, hat, and bass will be starting instruments.

    Returns: A pattern of the instruments in combination.
    '''

    def __init__(self, kick, snare, hat, bass):
        self.kick = kick
        self.snare = snare
        self.hat = hat

        self.bass = bass

    def instrument(self):
        print("PLAYING THE SOUNDFONT")

    def keys(self):
        print("I AM PLAYING THE", self.snare)


class Hip_Hop(TrapBeat):
    def __init__(self, kick, snare, hat, bass, trap_bass):
        super().__init__(kick, snare, hat, bass)
        self.trap_bass = trap_bass

    def keys(self):
        print("I AM PLAYING THE", self.snare, "WITH", self.trap_bass)


if __name__ == "__main__":
    soundfont = TrapBeat("High Kick", "High Snare", "High Hat", "Low Bass")
    print(soundfont.kick, soundfont.snare, soundfont.bass)
    soundfont.keys()
    soundfont.instrument()

    keys = Hip_Hop("Low Kick", "Mid Snare", "Low Hat", "Mid Bass", "Deep Bass")
    keys.keys()
    keys.instrument()

