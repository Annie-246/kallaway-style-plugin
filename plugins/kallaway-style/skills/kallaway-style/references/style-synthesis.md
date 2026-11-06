# Cross-video synthesis (corrected after independent review)

Sources: work/v1..v4/analysis.md and scene_log.csv. N of M counts unique videos (M = 4; 5.mp4 is a byte-identical copy of 3.mp4). No holdout exists because only 4 unique videos were supplied.
Class: SIGNATURE = 4/4 or central in 3/4. RECURRING = 2/4. ONE-OFF = 1/4.
Evidence: VERIFIED, INFERRED, UNKNOWN, carried from the per-video analyses.

## 1 Global numbers

| Metric | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| Duration, fps | 73.96, 24 | 38.85, 25 | 91.26, 24 | 89.83, 24 |
| Words / total duration (v4 includes ~36 clip words; speaker alone ~3.48) | 3.87 | 3.89 | 3.47 | 3.42 |
| Words / speaking time | 4.46 | 4.44 | 3.76 | 3.71 |
| Full-face share | 29% | 29.5% | 29.9% | 27% |
| Not full-face share | 71% (true split ~67%; rest meme/phone) | 70.5% | 70.1% | 73% |
| Face<->stage cuts per min | 14.6 | 10.8 | 9.2 | 6.0 |
| Longest face-free run | 9.5 s | 9.76 s | 15.6 s | 29.96 s |
| Words per caption screen | ~1.1 | 1.30 | ~1.0 | 1.27 |
| Caption median hold | 6 f | 6 f | 6 f | 8 f |

## 2 Scene taxonomy

| ID | Scene type | v1 | v2 | v3 | v4 | Class |
|---|---|---|---|---|---|---|
| ST1 | Full-frame speaker, caption only | yes | yes | yes | yes | SIGNATURE |
| ST2 | Dark split stage: graphics above, speaker cutout in bottom panel | yes | yes | yes | yes | SIGNATURE |
| ST3 | Persistent master diagram that evolves through the video | chart world | script card | timeline to tree | partial: chapter tiles, hawk to cone | SIGNATURE (3/4 full, 1 partial) |
| ST4 | Offer grid: real doc pages shown as volume | 9 | 5 | 14 | 9 | SIGNATURE |
| ST5 | Proof wall of many real reels | no: mock UI card | 6 | 6 | 5 | SIGNATURE (3/4) |
| ST6 | Real example inside a bordered card or window | no | profile only | yes | yes | RECURRING |
| ST7 | Light split stage | hook, doc, CTA | no | hook only | no | RECURRING |
| ST8 | Punch-in on face | step x1.19 | no | 10 f x1.11 | no | RECURRING |
| ST9 | Keyword chips in stacks | tags, pills | chips | pills | labels | SIGNATURE as a device, styling varies |
| ST10 | Numbered chapter tile that docks into a header | no | no | no | yes | ONE-OFF |
| ST11 | Meme or 3D collage cutaway | yes | no | no | no | ONE-OFF |
| ST12 | Literal object metaphor (brain, hawk) | no | no | no | yes | ONE-OFF, but see R8 |

## 3 Shared layout (SIGNATURE, 4/4)

| Item | v1 | v2 | v3 | v4 | Use |
|---|---|---|---|---|---|
| Panel x | 68-1012 | 71-1008 | 68-1011 | 67-1010 | 68-1011 |
| Panel top y | 1404 | 1408 | 1404 | 1398 | 1404 |
| Panel radius | ~44 | ~40 | ~44 | ~34 | 42 |
| Speaker rise above panel (varies with head) | 62-78 | 61-81 | 62-81 | 83-96 | ~80, v4 ~90 |
| Split caption centre y / height | 1241 / 44 | 1286 / 38 | 1276 / 42 | 1259 / 42 | per-video, default 1262 |
| Full caption centre y / height | 1156 / 50 | 1281 / 48 | 1210 / 49 | 1231 / 49 | per-video, default 1212; font = split x1.14-1.26 |
| Dark canvas (varies with glow) | #040404 | #0B0B0B | #060606-#090909 | #030303 | #030303-#0B0B0B |
| Dot pitch | 18.6 | ~40 | 18.6 | 15.4 | default 18.6 |
| Light canvas | #E1E1E1-#E3E3E3 | - | #E1E1E0 | - | #E1E1E1 |

All panels bleed off the bottom edge; the speaker is a matted copy drawn over the rounded panel so head and arms break its edges. Panel framing is locked; the speaker framing does not move during graphic transitions.

## 4 Typography (SIGNATURE, 4/4; fonts INFERRED)

- Closest match in all four: Inter Display/Inter Tight Bold-ExtraBold with tracking about -3 to -5%, plus Instrument Serif Italic. No overlay test was run, so font identity stays INFERRED.
- Serif italic marks the named concept or the word to remember: 4/4. Sans carries everything else.
- Titles: 2 centred lines near the top, Title Case, usually one serif phrase or one red accent. Title replays its reveal at each section entry: v2, v3, v4 explicit; v1 flicker-in at 3.96 and 21.2.

## 5 Colour (SIGNATURE)

- Near-black canvas with white text: 4/4.
- Red accent about #AC0001: 4/4 (v1 pill, v2 title highlight, v3 dot and banner, v4 banner).
- Secondary hues are semantic and per-video: v1 purple = attention, yellow = time segment; v2 rainbow legend for sections; v3 green = keep; v4 green = healthy comprehension. Rule: every extra hue must have one meaning for the whole video.
- Yellow highlight on a doc page: v1, v2, v4 (from the source docs, not a graphic).

## 6 Caption system (SIGNATURE, 4/4)

- Centred, white on dark and black on light, no stroke, no box, no pop, no active-word highlight.
- Hard swap on one frame, starting on the word within about 2 frames.
- Default one word per screen; short function-word pairs merge. Punctuation is kept. Digits are used for numbers.
- Exceptions: v1 list and meme lines use a word-by-word fade mode (38.33-39, 41.67-43.5); v1 43.6 giant word inside a phone; v2 0.24-2.2 and 36.12 hold three words.
- Holds on sentence ends. Serif key term may fade (v1 3.29, v4 3.83) or stack (v2 30.72).
- Captions run over everything, including clips (v4 S09).

## 7 Motion (SIGNATURE)

- Cuts: hard cuts only between layouts. No flash, dissolve-transition or whip between face and graphics, 4/4. Exceptions inside the stage: v1 whip f318, v1 43.6 clip shrinks into a phone, v2 whip A31, v4 zoom-through A25, v4 25.54 dissolve through a red-feathered freeze frame.
- Easing: fast-in with a long tail. v2 house curve (.3,0,.15,1); v3 default (.3,0,.1,1); v4 dock (.48,0,0,1); v1 default (.5,.05,.15,1). Default for the skill: bezier(.3,0,.15,1), 30-40 frames.
- Flicker-on: 4/4 as a device. Envelope varies. v4 [.3,.7,.5,.25,.65,1] measured identical on 4 elements; v2 [.35,.2,.3,.8,.3,.7,1]; v1 and v3 differ per instance.
- Element entry: opacity, small blur and a small shift for 5-8 frames, 4/4.
- Stagger: grids enter in reading order at 2-4 frames per item, 4/4.
- CONFLICT, overshoot: v1 none; v2 pages A34 overshoot 19 px. Default none.
- CONFLICT, motion blur: v1, v3, v4 blur fast moves; v2 none. Default blur on moves above 40 px per frame.
- Speaker camera: v1 punch and slow push; v3 tight cut, zoom and reframe at 3.04, 29.83, 75.54; v2 locked except a 31 px pan at the end; v4 locked. Default locked, punch only for the strongest lines.
- Stage camera: the graphics live in a world larger than the frame; the camera pans and zooms and titles may leave frame (v1 25.2, 36; v3 4.6, 41.8; v4 5.2). Slow drift while a diagram fills (v2 9.64-19.4, v4 13.1).
- Neon glow on lines, borders and tiles: v1, v2, v4. Sheen or sweep: v2 28.36, v3 f1458, v4 13-14, 79.46.

## 8 Sound (SIGNATURE for the logic, RECURRING for the palette)

- Music under voice with no ducking: 4/4 VERIFIED, except the clip section in v4.
- Median voice-over-music gap 13.5-19.6 dB; early v2 near 28 dB.
- Music runs to the last frame with no fade: v1, v2, v3 VERIFIED. v4 bed decays about 12 dB over the last 7 s.
- SFX mark graphic state changes. Plain returns to the face stay silent; thesis returns take a riser into music-off (v3 3.04, 29.83, 75.55). Clean in v1, v2. v4 10.42, 70.08, 82.08 show an 8-12 dB rise of unknown cause.
- Palette per video (all type names are guesses from spectrograms, nobody heard the audio): v1 3 low whooshes + 3 risers; v2 booms + pops; v3 about 15 soft whooshes + 3 risers; v4 impacts + whooshes + glides.
- Silence as emphasis: v1 3 drops, v3 3 drops, v4 1 long silence before CTA + dropouts, v2 none. RECURRING: 3/4 in some form.
- Riser into music drop into punch-in: v1, v3 (2/4). In both, the riser ends within a few frames of the cut or punch.
- SFX may land after the visual: v2 peaks +0.08-0.30 s. Type names are guesses from spectrograms; no audio was heard.

## 9 Placement rules

| ID | Rule | Evidence | Counterexample | N of 4 |
|---|---|---|---|---|
| R1 | Speaker steps out of the system to comment, judge or address the viewer: cut to the full face | v1 11.42, v2 5.72, v3 47.38, v4 43.04 | v1 56.0, v3 28.4, v4 39.5 | 4 |
| R2 | Cuts land 0-6 frames before the first word of a sentence (37 of 48 cuts) | v1 12/18, v2 5/7, v3 11/14, v4 9/9 | mid-sentence cuts mostly enter graphics: v1 1.75, 12.25, 20.5 | 4 |
| R3 | Items of a list get one visual move each, on or just before their word | v1 tags, v2 rows, v3 unblurs, v4 tiles | v3 80.14 | 4 |
| R4 | A named part reveals up to 0.46 s before its word, at most 2 f after | v1 7.16, v2 03.24, v3 39.02, v4 17.21 | v3 first example card +0.06 s is within tolerance | 4 |
| R5 | When a concrete thing is named, show the real thing | v2 32.24, v3 19.4, v4 26.9 | v2 18.4 | 3 |
| R6 | Offer: show many real pages in a grid, title "Comment" lands on its word | v1 71.71, v3 84.46, v4 77.5 | v2 says Comment in a stacked serif caption on the face, grid follows 1.52 s later | 3 |
| R7 | Frame 1 has a concrete visual; proof wall arrives by 2.4 s | v3 0, v4 1.5, v2 2.32 | v1 has no wall, its card shows the problem | 3 for wall, 4 for concrete visual |
| R8 | A verb of change: the graphic performs it | v1 "scroll away", v2 connector, v4 "decay", "dive" | v3 fixed nodes | 3 |
| R9 | Music drops under thesis lines on the face and returns on the next cut | v1 2.9-4.1, 25.8-27, 55.3-56.1; v3 3.2-4.7, 30-31.8, 75.7-79; v4 68.7-75.6 | v1 14.78, v3 63.17, none in v2 | 3 |
| R10 | Face does not return at a fixed interval | face-free runs up to 30 s (v4) | none | 4 |
| R11 | Graphic replaced by graphic gets an exit; graphic cut to face gets none | v2 02.24, 25.40 | not tested elsewhere | 1 |
| R12 | A new concept word goes in serif italic | v1 3.29, v2 0.36, v3 3.46, v4 3.83 | v4 17.2 "Visual Alignment" | 4 |
| R13 | Digits for spoken numbers | v1, v2, v3, v4 13.5, 79.75 | v1 "hundred.", "eight" 65.22 | 4 |

## 9b Techniques added by review

| Technique | Evidence | Class |
|---|---|---|
| CTA title: `Comment` + serif keyword in quotes + red line `To Get The Doc` | 4/4 | SIGNATURE |
| Blurred label hides the answer | v4 0-1.5, v3 37.6 | RECURRING |
| Progress bar | v1 27-60, v4 27.4-39.4 | RECURRING |
| Clips orbiting an axis or object | v1 12.25, v4 75.46 | RECURRING |
| Counting badge | v1 16, green view labels v3 1-3 | RECURRING |
| Speaker looks up at the clip, hands act out the graphic | v4 27.4-39.5, 56-59 | ONE-OFF |
| Serif notes beside an asset | v3 27.25 | ONE-OFF |
| Phone mockup with giant word | v1 43.6 | ONE-OFF |
| Face blurred in a card | v3 43 | ONE-OFF |

## 10 Structure template

Hook with a concrete visual (0-3 s) → name the idea (on the face in 3/4) → explain inside one evolving diagram, cutting to the face for verdicts → proof → offer grid with "Comment X" → cold end on the face or the grid. 4/4 end on an offer.

## 11 Not reproducible from this analysis

- Sheet timecodes run about 0.5 s late; use burst timecodes only.
- Fonts unverified. SFX and music files unknown. Speaker matte method unknown. No technique has been rebuilt or tested.
