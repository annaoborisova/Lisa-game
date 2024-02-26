# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define L = Character("Liz")
define Y = Character("You")
define T = Character("Thinking")
define N = Character("Narration")
define pov = Character("[playername]")
default Trust = 0
image Lizsprite = "sprite.png"
#to do: list of songs that ship crew blasted through bluetooth speakers, then use a loop to have Liz list them in dialogue
init python:
    Songs = ["XS by Rina Sawayama, ", "For What It's Worth by Placebo, ", "that one Eurovision song with the Pennywise knock-off, ", "Copy of a Copy by Nine Inch Nails, ", "Enter Sandman by Metallica."]

init python:
    def Trust3():
        if Trust > 3: 
            renpy.say(T, "Liz briefly lets down the veneer of professionalism and it’s obvious that she expects the adult in the room to know the answers. Getting there, but not quite yet.")
        else:
            renpy.say(T, "Liz seems to be holding together remarkably well for a twenty-year-old forced to face something deadly by the adults in the room. She deserves a solution, but there isn’t one in plain sight yet. Maybe she deserves some reassurance, in the meantime.")

init python:
    def Songsloop():
        for song in Songs:
            L (song)


label start:
show Lizsprite
L "Good day, can you hear me?"
#yes or no menu here
menu:
    "Yes":
        L "Alright, nice!"
    "No":
        L"Give me a second."
        N "She shakes and smacks her phone and the sound becomes clearer."


L "Oh, and before I forget, how do you pronounce your name again?"
#prompt for player name
python:
    playername = renpy.input("", length=32)
    playername = playername.strip()

    if not playername:
        playername = "P"
        
L "Nice to meet you, [playername]! I think we previously met during the orientation."


L "At any rate, I’m just calling you because one of the team leads is asking me to do something… unique and I thought you should know, as the designated mentor."
menu:
    "What kind of unique?":
        L "Well..."
L "In short, we have an infestation that survived the decontamination chamber."
L "And I’ve been asked to figure out how to remove it."
menu: 
    "You’re not an exterminator of any kind, you're an IT consulting intern.":
        L "Yeah..."
menu:
    "I’ll give HR a call after we get off the phone because this is crossing beyond the newbie hazing we've been trying to root out.":
        L "Thanks so much for that!"
menu:
    "In the meantime, what can I do for you?": #1
        $Trust += 1
    "Tell me more about this infestation.":
        $Trust += 1

L "It began with glitches in our entertainment system, and so far only the entertainment system."
L "Offline downloads of anything noisy and action-heavy are getting deleted or corrupted in ways that not even my boss here has seen."
L "And you know how long it takes to redownload video up here."
menu:
    "Yeah, it’s pretty obnoxious. And that’s a tech support, not an IT consulting matter.": #2
        $Trust += 1
    "You do know that unless there is an HR complaint, we are not to review staff browsing data, right?":
        L"Sorry, I thought we were allowed to access it for emergencies?"


menu:
    "Alright, so what else have you seen?":
        L "Slime that changes color depending on surrounding environment."
L "Staff started noticing it out of the corners of their eyes in the hallways."
L "Then it started hitching rides on their clothes to their rooms."
L "Microscopic amounts that our contaminant detectors aren’t trained on."
menu:
    "Is there a pattern to the sightings?": #3
        $Trust += 1
    "And the decontamination chamber didn’t flag it?":
        L "No, it seems that we have a first encounter."
L "In short, this thing is draining people." 
L "Three people with no health issues that the rest of the crew got warned about started fainting after any sort of minor exertion."
menu:
    "And they tested negative for COVID before the flight?":
        L "Yeah."
    "Sounds COVID-adjacent, but I am guessing that something else looks off as well?": #4
        $Trust += 1 
$Trust3()

N "Liz takes a deep breath."
L "They’re coughing up blood and black ooze beforehand."
L "And their eyes seem far off."
L "I can’t explain it, but it’s like you can see the void outside through them, when they’re coughing all of this up."
L "And then they stop abruptly."
L "And they just stare at you for a moment, and then they collapse."
menu:
    "Right, that’s… Terrifying":
        $Trust += 1
        L "Yeah, it really is." #5
    "Concerning, but hey, you know us, the Sharks. The toughest and most-coordinated ones around! We can get through this!":
        N "There is a far-off expression in Liz’s eyes that indicates complete disbelief."

L "We don’t know anything."
L "No one died yet, but our medical staff is at a loss, as this thing seems to be jumping between hosts."
L "It’s always three people, but their blackouts seem to last longer and longer."
menu:
    "When does it jump?":
        $Trust += 1 #6
    "Have we put everyone through decontamination?":
        L "We did, but it came back."
$Trust3()

L "Yeah, I noticed that it really hates loud noises."
L "When my boss first got infected and had her… attack, obviously someone started screaming."
L "So, the black chunks she coughed up moved."
L "Then, they slithered across the room."
L "Next thing we knew, they were crawling into that person’s mouth."
L "This person still can’t talk."
L "We don’t have any advanced medical equipment here, so it’s unclear if this is from shock or an actual internal injury."
menu:
    "Alright, we seem to be getting something resembling a complete picture here, thanks.":
        L "Yeah, no problem."
menu:
    "Do you think this thing understands our speech?":
        $Trust += 1
        L "Probably not yet. Hopefully. I don't know. It doesn't seem smart enough to bypass the Bluetooth speakers we leave blasting outside our rooms at night yet, at least." #7
    "I am sincerely hoping we don’t get a chestburster here…":
        L "Yeah, I’d say that we already had our precursor to the chestburster scene with that shushing."
L "But on the upside, this thing didn’t attack us when we were discussing trying to put that person through the decontamination again."
L "But the downside is that it’s one of those state-of-the-art noiseless setups."
L "And yeah, I don’t think it affects it."

#if/elif statement that checks trust points here
if Trust >= 5:
    jump good_ending
elif Trust >= 3:
    jump neutral_ending
else:
    jump bad_ending


label good_ending:
menu:
    "By the way, how many personal Bluetooth speakers does this ship have?":
        L "All the new hires and interns got them as welcome gifts at this retreat."
L "I’d say at least fifteen."
menu:
    "Grand. So, you and the other folks here will need to carry them all separately to the shuttle area and build a circle.":
        L "And then, impromptu concert time."
menu:
    "Yeah. And have some large food containers in there for trapping purposes.":
        L "Alright, gotcha."
L "We’ll try this tonight."
L "See you on Earth, hopefully."
L "Thanks."
$Songsloop()
L "Never want to hear them again after this."
return





label neutral_ending:
menu:
    "Listen, we can’t bring you all back to Earth yet. We don’t have a fully formed solution for this parasite yet. But we think we’ll have it in the next few days.":
        L "Right, makes sense."
menu:
    "So, just hang in there. You have been really brave and provided us a lot of valuable info, so you’ll all pull through.":
        L "Yeah, I thought we really had something here."
L "But I trust you."
L "I’ll keep sleeping with the Bluetooth speaker blasting outside my room, I guess."
menu:
    "Yeah, thanks so much for this. I’ll check in with you tomorrow as well. And the day after. Until we get you all out.":
        L "No problem and thanks for doing this."
L "Well, have a good day."
return






label bad_ending:
menu:
    "Listen, we don’t know what’s going on in the slightest. We can’t get you out yet, but we’ll be researching this issue continuously.":
        L "Right."
menu:
    "Just trust us. Please.":
        L "Sure."
L "Can our crew start doing daily check-ins with Earth, in the meantime?"
menu:
    "Yeah, although we can’t promise a definitive timeline for a solution. But we’ll start sending automated shuttles with additional food and medical supplies.":
        L "Sure, although I’m not sure how long the person who can’t speak will last."
L "And I’m not sure if this thing will wise up to our tactic of blasting music outside our rooms anytime soon."
L "But I guess I trust you."
L "Have a good one."
return