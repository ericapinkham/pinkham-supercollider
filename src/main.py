import time

import cowsay
import supriya

chords = {
    "C": [261.63, 329.63, 392.00],
    "Cm": [261.63, 311.13, 392.00],
    "C#": [277.18, 349.23, 415.30],
    "C#m": [277.18, 329.63, 415.30],
    "Db": [277.18, 349.23, 415.30],
    "Dbm": [277.18, 329.63, 415.30],
    "D": [293.66, 369.99, 440.00],
    "Dm": [293.66, 349.23, 440.00],
    "D#": [311.13, 392.00, 466.16],
    "D#m": [311.13, 369.99, 466.16],
    "Eb": [311.13, 392.00, 466.16],
    "Ebm": [311.13, 369.99, 466.16],
    "E": [329.63, 415.30, 493.88],
    "Em": [329.63, 392.00, 493.88],
    "F": [349.23, 440.00, 523.25],
    "Fm": [349.23, 415.30, 523.25],
    "F#": [369.99, 466.16, 554.37],
    "F#m": [369.99, 440.00, 554.37],
    "Gb": [369.99, 466.16, 554.37],
    "Gbm": [369.99, 440.00, 554.37],
    "G": [392.00, 493.88, 587.33],
    "Gm": [392.00, 466.16, 587.33],
    "G#": [415.30, 523.25, 622.25],
    "G#m": [415.30, 493.88, 622.25],
    "Ab": [415.30, 523.25, 622.25],
    "Abm": [415.30, 493.88, 622.25],
    "A": [440.00, 554.37, 659.25],
    "Am": [440.00, 523.25, 659.25],
    "A#": [466.16, 587.33, 698.46],
    "A#m": [466.16, 554.37, 698.46],
    "Bb": [466.16, 587.33, 698.46],
    "Bbm": [466.16, 554.37, 698.46],
    "B": [493.88, 622.25, 739.99],
    "Bm": [493.88, 587.33, 739.99],
}


# https://supriya-project.github.io/supriya/
@supriya.synthdef()
def simple_sine(frequency=440, amplitude=0.1, gate=1):
    sine = supriya.ugens.SinOsc.ar(frequency=frequency) * amplitude
    envelope = supriya.ugens.EnvGen.kr(
        envelope=supriya.Envelope.adsr(),
        gate=gate,
        done_action=2,
    )
    supriya.ugens.Out.ar(bus=0, source=[sine * envelope] * 2)


def play_chord(server, frequencies, duration=1):
    # Create an empty list to store synths in:

    synths: list[supriya.Synth] = []
    # Start an OSC bundle to run immediately:
    with server.at():
        # Add the default synthdef to the server and open a "completion" context
        # manager to group further commands for when the synthdef finishes loading:
        with server.add_synthdefs(supriya.default):
            # Loop over the frequencies:
            for frequency in frequencies:
                # Create a synth using the default synthdef and the frequency
                # and add it to the list of synths:
                synths.append(server.add_synth(synthdef=supriya.default, frequency=frequency))
    # Let the notes play for 4 seconds:
    time.sleep(duration)
    # Loop over the synths and free them
    for synth in synths:
        synth.free()


def main() -> None:
    # Create a server and boot it:
    server = supriya.Server().boot()

    # Define the chords for Pachelbel's Canon in D (according to copilot):
    canon_chords = [
        chords["D"],
        chords["A"],
        chords["Bm"],
        chords["F#m"],
        chords["G"],
        chords["D"],
        chords["G"],
        chords["A"],
        chords["D"],
        chords["A"],
        chords["Bm"],
        chords["F#m"],
        chords["G"],
        chords["D"],
        chords["G"],
        chords["A"],
    ]

    # Play the chords in a loop:
    for chord in canon_chords * 2:
        play_chord(server, chord, 1)

    # Wait a second for the notes to fade out:
    time.sleep(1)
    # Quit the server:
    server.quit()
    # Pachelbel's Canon in D (simplified version) as a list of (frequency, duration) tuples:


if __name__ == "__main__":
    cowsay.fox("What does Supriya say?")
    main()
