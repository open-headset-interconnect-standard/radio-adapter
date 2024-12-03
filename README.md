# Open Source OHIS Radio Adapter(s?)
An open-source OHIS Radio Adapter.

As of 2024-07-17, this is a Work In Progress.

# Goals

1. Design a set of circuits that can be used to build OHIS compliant radio adapters.
2. Designs should be as simple as possible, but no simpler.
3. When laying out boards, keep as many parts through-hole as possible for ease of assembly.
4. There are two types of designs here:
    1. **General:** Has all the circuits required to work with any radio, that needs to be configured.
    2. **Radio Specific:** Trades Configurability for Simplicity.  Make a simpler device for a specific radio.

# Directory Structure

All KiCAD projects are in their own subdirectories off the git root.  Where it makes sense to do so, an additional layer of subdirectory may be used to group several projects together more obviously.

`/Documentation/` and `/docs/` are reserved for documentation source, and documentation output, respectively.

Everything in `/docs/` will be published on github Pages.

## Icom, Yaesu, Kenwood

As of 2024-04-04, I (@SmittyHalibut, Mark Smith, N6MTS) have submitted three schematics (only!) for VERY SIMPLE radio controllers for the Big Three.  A few notes about these:

* **I HAVE NOT TESTED THEM!**  There's no guaranty that they'll work, or even that they won't blow up your radio.  (It most likely won't blow up your radio. Probably.  I think.  It might.  It shouldn't.  Yeah, probably not.  But there's no telling.)
    * If you find a better way to do any of this, please submit a Pull Request, or at least an Issue with your idea.
* **YOU HAVE TO VERIFY PINOUTS MATCH YOUR RADIO!**  I've selected pinouts for most modern versions of these radios, but while researching this, it becomes obvious that older radios were not so consistent, even within a given manufacturer.  (Yaesu seems to be the worst at this, but they all do it.)
    * See [EB3GKE's Mic Pinout Reference](Yaesu/EB3GKE Mic Pinout Reference.pdf), it collects a lot of pinout information.  **BUT THEY GET RJ45 PINOUTS WRONG**.  As far as I could see, all (only most?) of their RJ45 pictures number pins 1 through 8 backwards.  OHIS's schematics are absolutely correct (verified against TIA-568 documents), so if the pinout for your radio looks VERY DIFFERENT than OHIS's pinouts, try reversing the pin numbers and see if thats closer.
* As of 2024-04-04, I've only done the schematics, and even then it's little more than throwing notes down "on paper."  I tried to cover:
    * Connector pinouts (see above).
    * Any electrical circuits required (mostly converting from OHIS's electret level to dynamic level for radios that want dynamic.)

As of 2024-04-25, I (still @SmittyHalibut) laid out the boards described above and had them fabricated.

* **I STILL HAVE NOT TESTED THEM!**

As of 2024-07-17, I (still me) am chatting with @gx1400 about this.  I'm going to send him some of the boards I ordered back in April and he'll help me test.

As of 2024-12-03, I (STILL me) am sending hardware to @gx1400 and a few others for testing.  These tests are covering:

* Yaesu:
  * :check: RJ45 8p8c
  * :check: RJ14 6p6c
  * :green_square: GX16
* Icom:
  * :green_square: RJ45 8p8c
  * :check: GX16
* Kenwood:
  * :check: RJ45 8p8c
  * :check: GX16

If you can test Yaesu GX16 or Icom RJ45, please reach out to me.  @SmittyHalibut on github, or on Discord.

# Parts

Electrical components, in recommended order of assembly:
* 1x 2x2 pin header right angle
* 1x 2x4 pin header right angle
* 1x 1k axial resistor
* 1x 6.2k axial resistor
* 2x 100R axial resistors
* 2x 10uF
* 1x 1k pot
* 1x 5381 (RJ45 with LED) for OHIS socket

Mechanical components, same as User kit:
* 4x M3 6mm screw
* 4x M3 10mm screw
* 4x M3 14mm brass stand-off
* 4x M3 3mm ABS stand-off
* 5x .1" jumper

PCBs in this repo:
* 2x Top-bottom panels
* 1x Main board
* 1x Shim board

Radio Specific parts, in recommended order of assembly:
* 1x Radio Specific Board
* 1x 3.5mm TRRS "headphone/speaker" connector
* Microphone connector.  Either one of:
  * 5380 (RJ45 with no LED) or 5381 (with LED) if its easier, but the LEDs aren't used.
  * GX16 connector, and GX16 riser board

