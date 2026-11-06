# v1 reverse-engineering analysis

Source: `1.mp4`, 1080x1920, 24 fps, 73.96 s, 1775 frames. All pixel values are in 1080x1920 space. `fN` means frame N (t = N/24).
Labels: VERIFIED (measured or seen frame by frame, cited as v1 + timecode), INFERRED, UNKNOWN.
Measurement scripts and raw tracks are in `work/v1/tmp` (`track.csv`, `blobs.json`, `cam2.json`, `aud.npz`).
Whisper word times carry about +-2 frames of error, so word-to-visual offsets under 3 frames are treated as "on the word".

---

## 1 Summary

A 74-second educational talking-head short that teaches one idea (old story arc vs modern story arc) with a single evolving chart. The chart is the real protagonist: it occupies 56% of the runtime, and the speaker is reduced to a locked webcam card under it.

Key numbers (all VERIFIED, v1 whole video):

| Metric | Value |
|---|---|
| Shots | 20 |
| Hard cuts | 19, 15.4 per minute |
| Hard cuts + digital punch-ins | 21, 17.0 per minute |
| All edit events, adding whip f318 and phone zoom-out f1044 | 23, 18.7 per minute |
| Mean shot length | 3.70 s. Longest 179 f (7.46 s), shortest 20 f (0.83 s) |
| Dark chart split | 994 f, 41.4 s, 56% |
| Full-screen head | 521 f, 21.7 s, 29%, 9 shots |
| Light split | 193 f, 8.0 s, 11% |
| Meme + phone | 67 f, 2.8 s, 4% |
| Speech | 286 words, 232 wpm, no ducking |
| Captions | about 1.1 words per screen, median hold 6 frames |
| Sound effects | 3 low whooshes + 3 risers. Nothing on normal cuts |
| Music dropouts | 3 |

Signature techniques:
1. **One chart as a persistent world.** A virtual camera moves over it, and its state advances with the script across cutaways.
2. **Persistent lower deck.** Webcam card + caption never move during a hero transition, and a speaker cutout breaks out of the card's top edge.
3. **Silence as emphasis.** A short riser, then the music stem falls to -71 dB for about 1 s under the key line, then re-enters on the next beat.

---

## 2 Story structure against visuals

| Beat | Time | Script function | Visual | Colour state |
|---|---|---|---|---|
| Hook | 0.00-3.96 | "wrong story arc" claim | Real-looking retention UI, then head with punch-in and music drop | Light to dark |
| Old model | 3.96-11.42 | Teach 5 acts | Red bell curve, tags, camera follows each act | Black + red |
| Pivot | 11.42-12.25 | "But on social media" | Head | Dark |
| Why it fails | 12.25-19.0 | Cracked out brains, people scroll away | Collage whip to verdict; retention curve collapses over red arc; only Rising Action survives | Red + purple |
| Solution reveal | 19.0-24.7 | "use this" | Head, then white arc builds, then head with slow push | White on black |
| Hook phase | 24.7-32.1 | Starts at 70, first 5 seconds | Zoom to 70%, yellow bar, HOOK tag | White + yellow + purple tip |
| Peak 1 | 32.1-41.7 | Spike to 90, 3 methods | Stroke reaches peak, pan to pill list | Purple |
| Dopamine aside | 41.7-44.5 | Viewer brain | Meme to phone to "brain" | Skin tones, then light |
| Peak-release loop | 44.5-52.5 | Peak, release, repeat | Biggest zoom, stroke finishes curve, 9-bar timeline completes | Purple + yellow |
| Principle | 52.5-61.2 | Stack mini peaks | Punch-in + music drop, then area fill | Solid purple |
| Offer | 61.2-71.7 | Doc of 8 principles | Light doc grid, then head with slow push | Light |
| CTA | 71.7-73.96 | Comment "Story" | Same grid rebuilt with CTA title | Light |

Structural logic (INFERRED): colour tracks the argument. Light bookends frame the video as "documents and evidence". Red means old and failing. Purple means retention, seeded in the first 0.5 s as the magenta curve on the UI card and paid off at 57-61 s. Yellow only ever means "time segment that holds attention".

---

## 3 Scene types seen

### Shared lower deck (all split scenes)

- **Webcam card:** x 68-1012 (6.3%-93.7% W), top y 1404 (73.1% H), bleeds off the bottom. Top corners radius about 40 px, measured from the curve at y 1405-1445. VERIFIED v1 1.6.
- **Footage inside the card:** locked. Lamp centroid stays at (947.9, 1520.0) +-0.2 px in 12 of 13 sampled frames from 1.6 to 73.5 s (the 28.0 sample was occluded). VERIFIED. There is never a zoom inside the card.
- **Scale:** the head shot is 2.55x the card shot (template match cc 0.996, f41 to f42). VERIFIED. 944 px wide at 16:9 gives 531 px tall, so the card is the whole landscape source with about 15 px off-canvas. INFERRED.
- **Breakout matte:** head rises to y about 1320 (84 px, 4.4% H above the card), and hands and arm extend beyond the top and right edges. Example v1 4.5 hand reaches y about 1290; v1 0.5 arm passes x 1012. VERIFIED. It needs a person matte drawn over a rounded-corner clipped copy.
- **Caption:** centred, y centre 1241 (64.6% H). Drawn above the hand. VERIFIED at v1 4.70 (one frame).

Rebuild in Remotion, bottom to top: hero `AbsoluteFill`; `<OffthreadVideo>` clipped by a rounded div at top 1404, left 68, width 944; the same video with an alpha matte, unclipped; caption layer.

### T1 Light split (0.00-1.75, 63.54-67.58, 71.71-73.96)

- **Background:** #E1E1E1 to #E3E3E3, with a fine dot-grid texture on an 11 px period and a faint line grid on about 19-20 px (autocorrelation, std 3.4 levels). Use a tiled PNG.
- **Title:** line 1 y 132-181, line 2 y 194-257, x 217-861 (59.6% W). Black #010101, accent red #AF0006. Line pitch 62 px, about 66 px font (3.4% H), INFERRED from height.
- **Caption:** black, x centre 539, y 1219-1263.
- **UI card (hook):** final white area x 297-781, y 300-1156 (44.8% W, 44.6% H), #FDFDFD, outer grey frame #BBBBBB about 3-4 px, offset 12 px outside the white. Contents: "Reel insights" header, a thumbnail of the speaker, retention chart with magenta #D900E5 stroke 7 px plus about 25 px soft glow, skip rate rows 28.8% vs 49.2%. VERIFIED v1 1.6.
- **Doc grid:** 9 white cards 228x209 px at x 174/426/678, y 348/587/832 (gaps 24 px horizontal, 30-36 px vertical). Highlight #F0FF59 on page 9. VERIFIED v1 67.0.
- **Timing:** see A01-A04, A34, A35.

Why this design (INFERRED): a screenshot-like retention graph is proof, and it names the viewer's own pain in the first second. Light background in the hook stands out against dark feeds and sets up the hard contrast of the first cut. Light returns only for the doc because it reads as paper: it says "this part is a thing you take away".

### T2 Full-screen head (9 shots)

- Crop 2.55x of the card scale, no background change, footage already has shallow focus.
- Caption white, centred, y 1131-1181 (centre 60.4% H), sits on the dark shirt collar. Font is 1.155x the split caption ("modern" 252 vs 218 px wide). VERIFIED v1 21.8 and 22.72.
- Three motion modes: locked (6 shots, 2 of them with a punch-in), punch-in x1.19 at f67 or x1.185 at f1323, slow push x1.08-1.12 at f540, f1468, f1622.
- No B-roll overlays, no graphics, no emoji on any of the 9 shots.

Why (INFERRED): after charts, the face gives relief and re-establishes the human. It always carries the pivot sentence, the moment where the viewer needs a person telling them what changes next.

### T3 Dark chart, traditional (3.96-11.42, verdict 14-19)

- **Background:** #040404 with a dim dot grid (dots peak about #101010, median #050505). Radial glow in the line colour behind the chart.
- **Title:** "Traditional" bold sans + "Story Arc" serif italic. x 178-904, starts y 289, moves up to y 178 at f161-f180.
- **Axes:** white 3-4 px, x axis at y 954, y axis at x 168, tips fade out. Pink-tinted by glow.
- **Line:** #E5000A bright core, 5-6 px, red glow extending about 60 px. Dimmed state #4B0006.
- **Nodes:** white circles, 18 px at S=1, soft bloom.
- **Tags:** white rect, black bold text about 30 px, pointer tail, placed beside each node. Blur-in with width wipe.
- **Verdict title:** "This Traditional Story Arc" x 173-905, y 229-286. Pill x 234-845, y 290-376 (56.6% W, 4.5% H), #AC0001, radius about 10 px, white text.
- **Badge:** #AC0001 pill 176x54 px with eye icon and count, rides the tip of the purple curve.

Why this animation (INFERRED): a line tracing left to right is the exact form of the thing being taught. Red signals "old/danger" before the speaker condemns it, and the tags land on the words so the chart works as a slide being taught live. Dimming the red arc on "no longer" kills the model visually. The retention curve then crosses it and leaves only the rising segment lit, which answers "before the rising action ever gets good" with geometry.

### T4 3D collage (12.25-13.2)

Four vertical clips (about 288x500 px) with 3 px white frame and small radius. Each shows a "person drowning in phone content" image or clip with light motion. Arrangement at t=13.0: top centre (308-596, y 195-630), right (590-877, y 350-852), left (150-440, y 475-975), bottom (430-722, y 632-1132). VERIFIED v1 13.0. Layer order: bottom card over left over top. Group rotates around the Y axis: the frontmost card travels right to left at 12.25-12.75 with heavy motion blur, then settles into a slow drift.

Why at this word (INFERRED): "cracked out brains" is the one abstract insult in the script. It gets the only literal imagery in the first 40 seconds, and the rapid rotation is the mental state itself.

### T5 Dark chart, modern (20.5-22.5, 24.7-32.1, 34.96-41.67, 46.54-52.54, 56.0-61.17)

- **World:** one 1080x1384 container, scale pivot exactly (540, 692). Proof: at f1120-f1195 tx and ty stay under 2 px while S goes 1 to 1.54. VERIFIED. 1384 is the height above the webcam card, so the pivot is the container centre (the container reading is INFERRED).
- **Title in world:** "Modern" sans + "Story Arc" serif, x 244-835, y 280-339 at S=1. Scales with the camera, unlike T3, where the title is screen-locked.
- **Axes at S=1:** y axis x 168, x axis y 954.
- **Nodes at S=1 (world coordinates):** start about (168,643) on the y axis (back-projected from the hook framing), peak (327,496), trough (406,800), peak (479,624), trough (565,836), peak (667,630), trough (723,793), peak (800,693). Then a free tail ending about (945,950). Node 24 px diameter.
- **Line:** thin grey-white stroke 2 px, then purple #D300E1 core, 5 px, bloom #A400CA, 40-60 px.
- **Tag:** "70%" white bold italic-looking small text left of the start node.
- **Timeline bars:** under x axis, 9 segments, yellow #F9EE08-#FAF40A, grey #ABAAAA, height 16-20 px at S=1, gaps 3-4 px, glow on yellow. Order: Y Y G Y G Y G Y G(long).
- **Fill:** #A400CA, area between the curve and a horizontal threshold about 85 px below the start node (world y about 728). VERIFIED v1 59.0.
- **Pills:** 512x90 px on screen (camera about S=1.45), #3F3F3D to #434343, top-edge light, white bold text with soft bloom, stacked about 127 px pitch. VERIFIED v1 38.7, 40.2.

Why (INFERRED): the same white curve is first shown cold, then painted purple only where the script has reached. The viewer watches their own position in the video. It turns explanation into a progress bar, which is itself a retention device. Yellow bars under the axis are a second encoding of "peak vs release", so the graph is readable when zoomed in.

### T6 Meme full bleed (41.67-43.5)

Grainy upscaled clip of a bearded man staring at a phone, flat tan background. Caption multi-word, fades word by word on two lines at y about 918 and 980. "dopamine" in serif italic.

Why (INFERRED): the first non-speaker face at the 57% point, used as a pattern interrupt right after the pill list and right on the "dopamine hit" line. The meme itself is a person getting that hit.

### T7 Phone mockup (43.54-44.46)

Meme shrinks into a black notched phone frame (x 160-918, y 188-1728) on the T1 light background. The clip dims to about 25% luma (82 to 20). "brain" in heavy tight sans x 268-835, y 819-1009 (52.5% W, 9.9% H). "in the viewers" small above, top-left aligned with the b ascender. VERIFIED v1 44.3.

Note a tiny black square artifact at about (885, 212) on the phone corner. VERIFIED. It looks like an unmasked layer, do not reproduce it.

---

## 4 Typography

| Role | Font | Evidence |
|---|---|---|
| Title sans, caption, tags | INFERRED: Inter Display or Inter Tight, Bold to ExtraBold, tracking about -3 to -5% | Double-storey a, flat terminals, tight setting. Letterforms cannot separate Inter from close neo-grotesques at this size, so not VERIFIED |
| Serif italic: "Story Arc", "story arc.", "dopamine", "HOOK", "Story" | INFERRED: Instrument Serif Italic, closest match. Condensed, high contrast | Not proven by glyph overlay |
| "brain" display word | INFERRED: same family at Black, tracking near -8%, letters touching | Possibly a Helvetica-type Black; UNKNOWN |

Sizes (font sizes INFERRED from measured bbox heights; bboxes VERIFIED):

| Element | Bbox height | Font size | % H |
|---|---|---|---|
| Light title | 50 px line 1 | about 66 px | 3.4 |
| Dark title sans | 58 incl. descender | about 62 px | 3.2 |
| Serif italic pairing | | about 1.35x the sans size | 4.4 |
| Split caption | 45 px "attention" | about 62 px | 3.2 |
| Full caption | 1.155x split | about 72 px | 3.7 |
| "brain" | 190 px | about 245 px | 12.8 |

Rules seen:
- Sans for facts, serif italic for the concept being named. The pairing "Traditional *Story Arc*" and "Modern *Story Arc*" keeps the object constant and swaps the sans adjective.
- Title Case in all titles and tags, sentence fragments with punctuation in captions (whole words carry their comma or full stop).
- One accent colour per title: red word(s) on light, red pill on dark.

---

## 5 Colour

| Token | Hex | Use | Status |
|---|---|---|---|
| Ink black | #010101 | Text on light | VERIFIED |
| Canvas dark | #040404 | Dark scenes | VERIFIED |
| Canvas light | #E1E1E1-#E3E3E3 | Light scenes | VERIFIED |
| White | #FFFFFF | Text, nodes | INFERRED (nodes clip to max) |
| Red on light | #AF0006 | Title accent | VERIFIED |
| Red pill | #AC0001 | Pill, badge | VERIFIED |
| Red line | #E5000A | Old arc | VERIFIED |
| Red dim | #4B0006 | Dead arc | VERIFIED |
| Magenta on light | #D900E5 | UI retention curve | VERIFIED |
| Purple line | #D300E1 / #CB00DF | Retention curve, modern arc | VERIFIED |
| Purple fill | #A400CA | Area fill | VERIFIED |
| Yellow | #F9EE08-#FAF40A | Peak bars | VERIFIED |
| Grey bar | #ABAAAA | Release bars | VERIFIED |
| Pill grey | #3F3F3D-#434343 | List pills | VERIFIED |
| Highlight | #F0FF59 | Doc page marker | VERIFIED |
| Frame grey | #BBBBBB | UI card edge | VERIFIED |

The palette is 2 canvases plus 3 semantic hues (red = old/verdict, purple = attention, yellow = time segment). The speaker footage is warm orange skin on black with cyan and yellow background lights, so the overlays are chosen outside skin hues. INFERRED.

---

## 6 Motion and transitions

Cut grammar: 19 of 19 scene changes outside the whip and phone zoom are hard cuts with no flash, no blur and no fade. VERIFIED from cuts.json against bursts.

False positives dropped from cuts.json: f67 (punch-in, kept as its own class), f82-83 (hand), f297-322 (collage), f1044-1054 (phone zoom), f1323 (punch-in, own class).

Camera on the chart, per-frame similarity fit on nodes, 3+ inliers, residual under 5 px (VERIFIED):

| Move | Frames | S from-to | Translate at end | Bezier fit | t at 50% |
|---|---|---|---|---|---|
| 25.2 zoom | 600-632 | 1.00 to 1.50 | tx +395 | .73 .02 .28 .98 | 0.50 |
| 26.5 tilt | 632-672 | 1.50 to 1.58 | ty -220 | .38 -.04 .29 .90 | 0.40 |
| 35 zoom | 843-895 | 1.00 to 1.45 | tx +217, ty -16 | .44 .05 0 1.14 | 0.28 |
| 47 zoom in | 1119-1165 | 1.00 to 1.54 | none | .54 .05 .13 1.05 | 0.37 |
| 48.6 zoom out | 1166-1195 | 1.54 to 1.00 | none | .44 .09 0 1 | 0.28 |
| 57 zoom in | 1364-1405 | 1.01 to 1.14 | tx -19 | .38 .29 .09 .96 | 0.27 |
| 59.6 zoom out | 1428-1462 | 1.13 to 1.00 | tx -19 kept | ease-out (fit invalid) | 0.22 |
| Traditional stops | 18-22 f each | see A06-A11 | | about .30 0 .30 1 | 0.35 |

Summary: moves are long (18-46 frames) with slow start, fast middle and a long tail. There is no overshoot and no spring. A single usable default for chart camera moves is `Easing.bezier(.5,.05,.15,1)`; use .73 .02 .28 .98 for the slower anticipation variety.

Chart camera always resets to S=1 after a cutaway (f593, f839, f1117, f1344). Stroke and bar state do not reset. VERIFIED.

Punch-ins: 1 frame, x1.19, no ease, on a stressed word, both paired with a music drop.

Slow pushes: scale grows with acceleration rather than decelerating (gap metric 632, 638, 638, 648, 660, 668, 676, 694, 706 at 6-frame steps on f540-f593). Use `Easing.in(Easing.quad)` from 1 to the end value. They end on a hard cut at speed, so the cut feels like release of the push. INFERRED.

Entry style for all small UI elements: opacity + blur + small movement together for 5-8 frames. No bounce anywhere.

Flicker in: titles at f95-104 and f510-519 strobe in rather than fade. Normalised max-luma: f95 .44, .38, 1, .54, .58, .87, .65, .76, .89, 1; f510 .55, .90, .96, .49, .81, .69, .87, .95, .95, 1. VERIFIED.

Whip: slides the hero world only, lower deck stays. About 870 px, directional blur f318-f328, tail to f356.

---

## 7 Caption system

- **Mode A, word swap (most of the video):** one word at a time, hard swap, no animation, no highlight, no pill. Caption events within +-2 frames of a Whisper word start in 87% of detected changes. Median offset -0.003 s. Median hold 6 frames. VERIFIED.
- **Groups:** short function-word pairs stay together: "The reason", "we were", "want to", "It actually", "of a", "you need", "you go", "the climax", "over and", "as you", "if you want", "that you can", "It's kind of", "and I'll". About 1.1 words per screen, INFERRED from counting these against 286 words.
- **Spelled-out numbers:** "hundred." is written while "70" and "90" stay as digits. "rehooking" joined.
- **Mode B, key term:** phrase set in serif italic and faded in word by word: "story arc." at 3.29-3.96 (f79-f95). Fades about 4 frames per word. VERIFIED.
- **Mode C, phrase reveal (list and meme):** the line is laid out for the final phrase and unrevealed words are transparent, so text does not reflow. "contrarian statements," 39.5-40.5 sits left of centre then completes. Meme lines grow the same way. VERIFIED v1 39.5-40.0, 41.8-43.3.
- **Colour:** white on dark, black on light, no outline, at most a faint shadow. INFERRED.
- **Position:** split 64.6% H; full 60.4% H; meme 47.8% H.
- **Anomaly:** caption shrinks to 0.32 scale at 38.33-39.25 ("contrast", "contrast moment,"), a width of 158 px where about 495 px is expected. Looks like a scale keyframe error, not a choice. INFERRED. Do not reproduce it.

---

## 8 Asset treatment

- **Speaker:** one landscape source, static framing. All framing is digital. VERIFIED by locked lamp position and scale factor. Pause removal: UNKNOWN. Hand pose is continuous across the split/full cut at f41/42 (VERIFIED there only), which suggests the two layouts are crops of the same take. INFERRED.
- **Matte:** person segmented on every split frame, including motion-blurred hands (v1 0.5, 5.9). Edge quality is good, with no visible halo at 1:1. Tool UNKNOWN.
- **Mock UI:** "Reel insights" card is rebuilt, not a screenshot. Evidence: animated curve and rows, clean vector text. INFERRED.
- **Collage clips:** 4 clips, heavily styled, soft upscaled look; possibly AI-generated. INFERRED.
- **Meme:** low-res clip upscaled, visible grain added or retained. Full bleed.
- **Doc pages:** real document screenshots shrunk until illegible. Reading is not the point; quantity is. INFERRED.

---

## 9 Sound and music

Levels from stems, 20 ms RMS (VERIFIED):
- Vocals: median about -29.5 dB, p90 about -23 dB.
- Music stem: median -38.8 dB, p90 -36.5 dB.
- Median speech-to-bed gap about 9-10 dB; peaks about 15 dB.
- Energy almost entirely under 150 Hz (band median -40 dB) with 150-800 Hz at -52 dB: a dark sustained bass/organ bed. Upper bands under -80 dB.

No ducking. Low band speech-on vs speech-off medians differ by 0.0-0.5 dB across 14-55 s. Correlation of stem level to voice level -0.17 to +0.04. VERIFIED.

Timeline:

| Time | Event | Hits | Status |
|---|---|---|---|
| 0.00-2.86 | Thin bed, no bass tone | Hook | VERIFIED |
| 0.14-0.60 | Low whoosh swell, peak 0.32 at -27 dB | Hero scale-in and title fade | VERIFIED, type INFERRED |
| 2.38-2.85 | Rising sweep to about 6 kHz | Leads punch-in 2.79 on "wrong" | VERIFIED, type INFERRED |
| 2.86-4.00 | MUSIC DROP, -71 dB | "wrong story arc." | VERIFIED |
| 4.00 | Bass bed enters hard | Hard cut to black chart | VERIFIED |
| 4.0-11 | Bed rises from -47 to -38 dB | Chart builds | VERIFIED |
| 13.0-13.6 | Low whoosh, peak 13.28 at -26.7 dB | Whip slide | VERIFIED, type INFERRED |
| 25.30-25.75 | Rising sweep | Zoom to 70% | VERIFIED |
| 25.78-26.90 | MUSIC DROP | "70 out of 100." | VERIFIED |
| 26.9-27.2 | Bed returns over about 8 frames | "The first five seconds" | VERIFIED |
| 37.98-38.25 | Low whoosh, peak 38.12 at -27.2 dB | Pan to pills | VERIFIED |
| 54.9-55.2 | Rising sweep | Punch-in 55.125 on "middle" | VERIFIED |
| 55.20-56.04 | MUSIC DROP | "of the story." | VERIFIED |
| 56.04 | Bed hard return | Cut to full arc on "Instead" | VERIFIED |
| 57.68 | Low-mid hit -25.5 dB | Fill wipe. May be music or bleed | UNKNOWN |
| 58-73.96 | Bass pulses about every 0.68 s (about 88 BPM) | Offer section | Pulses VERIFIED, tempo INFERRED. audio_metrics tempo 117 looks speech-driven and is not trusted |
| 73.96 | Music plays to last frame | No fade | VERIFIED |

Sound effects total: 3 low whooshes + 3 risers. No clicks or pops on node reveals, tags, pills, doc pages or hard cuts: the detector found no transient in no_vocals at those timecodes. VERIFIED for that stem; a very quiet SFX folded into the vocals stem is UNKNOWN.

---

## 10 Placement decision rules

1. **When the speaker starts a pivot sentence, cut to the head.**
   Evidence: 11.42 "But", 18.96 "So", 32.08 "Then", 44.46 "Now", 52.54 "In the modern era", 61.17 "Now". Also 22.5 "The modern story arc" and 67.58 "It's kind of".
   Counterexample: 1.75 cuts to head mid-sentence on "is because", and 56.0 "Instead" (a pivot word) goes to the chart.
2. **When the speaker starts the first concrete claim after a pivot, cut back to graphics 2-6 frames before the word.**
   Evidence: 3.96 before "This", 12.25 before "with", 20.5 before "you", 24.71 before "It", 34.96 before "you", 46.54 before "boom", 56.0 before "Instead", 71.71 before "Comment".
   Lead measured 0.07-0.26 s. Counterexample: none in this video.
3. **When the speaker names a chart element, reveal it on that word; do not lead by more than 8 frames.**
   Evidence: tags 7.16, 8.14, 9.14, 9.98, 10.84; "70%" at 25.74; pill 3 at 40.72.
   Counterexample: "HOOK" reveals 27.75, 0.29 s before the word; "Contrarian Take" begins at 39.08, 0.40 s before; "brain" appears 0.5 s before Whisper's word start.
4. **When the speaker gives a number or end-state, the camera arrives on it.**
   Evidence: zoom midpoint 25.63 to "70" 25.74; stroke hits peak on "spike" 35.46, settles by "90" 36.38.
   Counterexample: "five to ten seconds" at 34.1 has no graphic because it is on the head.
5. **When the speaker makes the single strongest line in a section, cut the music for about 1 s and precede it with a riser.**
   Evidence: 2.86, 25.78, 55.20. Spacing 23 s and 29 s.
   Counterexample: "No longer works" 14.78 is a strong line and gets a visual dim only.
6. **When a sentence is about to land and the speaker stays on the head, use a punch-in on the stressed word.**
   Evidence: 2.79 "wrong", 55.125 "middle". Both in full-screen shots and both within 2 frames of the riser end.
   Counterexample: other pivot shots have no punch.
7. **When the head shot is setup with no stress word, use a slow push.**
   Evidence: 22.5, 61.17, 67.58.
   Counterexample: 11.42, 18.96, 44.46 appear locked (all but one under about 2.1 s; 11.42 and 18.96 by gap metric only).
8. **When the speaker says something physical about change, the graph itself does it.**
   Evidence: "no longer" dims the arc, "scroll away" drops the curve, "back up" zooms in, "stacking" fills the area, "over and over" extends the stroke, "dropped in the middle" starts the purple at the mid-height node.
9. **When the speaker uses vivid slang or an aside, leave the chart for 1 asset.**
   Evidence: 12.25 collage on "cracked out brains", 41.67 meme on "hit of dopamine". Both last under 3 s, and both end in a transformation inside the same shot, not a cut.
10. **When a real thing is offered, go light.**
    Evidence: 63.54 doc, 71.71 CTA. Light also opens the video at 0.00.
11. **Hand gestures are not used as triggers.**
    Spot-checked at 4.3 (pointing up) and 25.0 (raised palm): the graphics do not align. Rule is word-driven. INFERRED.
12. **SFX only marks hero-space movement.**
    Whooshes 0.32, 13.28, 38.12 sit on large world moves.
    Counterexample: the 25.2 zoom gets a riser and the 47 zoom gets nothing.

---

## 11 Animation inventory

Times in seconds, frames at 24 fps. Scene type refers to section 3. Start, end and script line are VERIFIED from bursts; intermediate frame numbers are read at the burst's sample rate, so treat them as +-2 frames unless they come from a numeric track (camera, count, card width, phone edge).

| ID | Start | End | Frames | Scene | Script line | Keyframes | Rebuild |
|---|---|---|---|---|---|---|---|
| V1-A01 | 0.00 | 1.67 | 40 | T1 | "The reason your videos" | Card width 300 (f0), 322 (f6), 368 (f9), 409 (f12), 448 (f18), 460 (f21), 484 (f39). Height 530 to 856 | Scale .62 to 1 pivot (540,729) with `bezier(.5,.05,.15,1)` |
| V1-A02 | 0.10 | 0.60 | 12 | T1 | "The reason" | Title opacity 0 at f2, about 50% f7, 100% f13, slight blur | Opacity 0 to 1 + blur 6 to 0 px, moves with A01 world |
| V1-A03 | 0.25 | 0.80 | 13 | T1 | "your videos" | Card rows stagger: back button f1, header f3, Retention f8, thumb f8-f11, axes f9-f11, skip rows f12-f16 | Stagger of opacity + blur, 2-3 frames apart |
| V1-A04 | 0.46 | 1.25 | 19 | T1 | "videos don't hold" | Magenta tip: f11 start, f13 mid-drop, f18 elbow, f30 end | Stroke-dashoffset, `Easing.out(cubic)` |
| V1-A05 | 3.96 | 5.96 | 48 | T3 | "This is what we were all taught" | Title flicker f95-104; origin dot f96; axes f97-f110; line f99-f143; nodes pop f107, f112, f119, f142 | Dash reveal on path; nodes opacity pulse with bloom |
| V1-A06 | 6.75 | 7.46 | 18 | T3 | "story arc. Initial conflict" | S 1 to 1.156, tx +181, ty -80; title y 289 to 178 | World scale with focus at origin; title separate |
| V1-A07 | 6.92 | 7.25 | 8 | T3 | "Initial conflict" | Tag narrow bar f166, half f170, full f173 | scaleX from left + blur + opacity |
| V1-A08 | 7.88 | 8.30 | 10 | T3 | "rising action" | tx 180 to 139, S 1.16 held; tag f193-f200 | Pan + tag |
| V1-A09 | 8.83 | 9.33 | 12 | T3 | "climax" | S 1.158 to 1.13, tx 125 to 10, ty -76 to +28; tag f218-f224 | Pan down |
| V1-A10 | 9.62 | 10.33 | 17 | T3 | "falling action" | S 1.133 to 1.20, tx 3 to -226, ty 28 to -85; tag f236-f243 | Pan right |
| V1-A11 | 10.54 | 11.12 | 14 | T3 | "resolution." | S 1.197 to 1.0, tx -226 to 0, ty -85 to 0; tag f260-f264 | Return to rest |
| V1-A12 | 12.25 | 13.17 | 22 | T4 | "with our cracked out" | f294 flat 4 cards; f297-f308 fast Y orbit with blur; f308-f316 slow drift | CSS 3D `rotateY` on 4 planes at radius about 250 px, `perspective` about 1400 px, motion blur via subframe samples (rebuild values INFERRED) |
| V1-A13 | 13.17 | 14.83 | 40 | T4 to T3b | "brains, this five-act" | Title x0 at f328 387, f332 313, f336 265, f340 229, f344 205, f348 190, f352 180, f356 174 | translateX of hero, `Easing.out(quint)`, directional blur first 10 frames |
| V1-A14 | 13.25 | 14.25 | 24 | T3b | "this five-act story" | Red line retrace during A13 | Re-run A05 line; nodes pop in sequence |
| V1-A15 | 14.90 | 15.33 | 10 | T3b | "no longer" | Stroke falls to #4B0006, glow off | Opacity to about .25 |
| V1-A16 | 15.83 | 17.50 | 40 | T3b | "Because most people scroll away before" | Count 3790, 3039, 2385, 1930, 1588, 1316, 1095, 912, 758, 629, 520, 427, 350, 286, 233, 190, 157, 132, 114, 104, 100 at 2-frame steps | Curve y exponential; badge rides tip; interpolate the listed count values directly |
| V1-A17 | 16.12 | 18.0 | 45 | T3b | "scroll away before the rising" | S 1 to 1.149, tx 0 to +79 | Slow drift |
| V1-A18 | 17.45 | 17.92 | 11 | T3b | "rising action" | Segment node 2 to 3 relights red | Duplicate stroke clipped to segment, grow from left |
| V1-A19 | 20.50 | 21.75 | 30 | T5 | "you want to use this, the modern" | Nodes pop in non-linear order f492-f502; axes f493-f508; labels partial "Plot", "Over" then full at f503; line f498-f524; title flicker f510-f519 | Node stagger, then dash reveal |
| V1-A20 | 25.17 | 26.17 | 24 | T5 | "starts at 70" | f604 S 1.008, f612 1.09, f618 1.346, f622 1.444, f628 1.492 | Zoom with tx, blur during peak speed |
| V1-A21 | 25.60 | 25.75 | 4 | T5 | "70" | "70%" tag fade, node glow | Opacity |
| V1-A22 | 26.54 | 27.92 | 33 | T5 | "out of 100. The first five" | ty -16 to -220 | Tilt |
| V1-A23 | 26.92 | 27.00 | 3 | T5 | "The first" | Yellow bar 1 fade | Opacity |
| V1-A24 | 27.40 | 29.45 | 49 | T5 | "seconds, the hook" | Arrow draw f658-f666 with loop; HOOK fade f666-f670; out f703-f707 | SVG path draw; serif text |
| V1-A25 | 28.90 | 35.50 | 158 | T5 | "dropped in the middle ... spike" | Purple tip from 70% node; 31.5 at dip; 35.0 near peak; 35.5 at peak | Stroke progress driven by word timecodes, continues during cutaways |
| V1-A26 | 35.17 | 37.50 | 56 | T5 | "spike the viewer to 90 out of 100" | Zoom table row 35; bar 2 fade f840-f846; node bloom from f880 | Zoom + glow |
| V1-A27 | 37.75 | 38.75 | 24 | T5 | "first peak. A contrast" | y axis x 226 f906, 272 f911, 776 f919, 832 f922, 898 f929; connector extends left f905-f917 then drops f917-f923 | Pan with blur f912-f918; two-part path draw |
| V1-A28 | 38.10 | 41.00 | 70 | T5 | "contrast moment, contrarian, shocking stat" | Pill 1 f915-f928, pill 2 f941-f954, pill 3 f969-f984 | Opacity + blur 12 to 0 + small x move |
| V1-A29 | 41.75 | 43.54 | 43 | T6 | "something to release that initial hit of dopamine" | Words fade about 4 f each, text out f1041-f1045 | Phrase reveal, Mode C |
| V1-A30 | 43.50 | 44.21 | 17 | T6 to T7 | "in the viewer's brain" | Screen left edge x 19 f1047, 54, 78, 96, 109, 120, 129 f1053; luma 82 f1043 to 20 f1049; brain opacity f1048-f1060 | Scale from about 1.9 to 1 with `Easing.out(cubic)` |
| V1-A31 | 46.54 | 51.20 | 112 | T5 | "boom, you go back up ... peak" | Stroke past trough at cut; peak 2 at about 47.8; trough 49.7; peak 3 50.0; finish tail 51.2. Bars f1118-f1128, f1184-f1192 | Stroke progress keyed to words |
| V1-A32 | 46.75 | 49.54 | 67 | T5 | "back up for another peak" | Zoom in + zoom out table | Pure scale about (540,692) |
| V1-A33 | 57.00 | 58.33 | 32 | T5 | "stacking mini peaks on top" | S table; fill wipes left to right f1374-f1400 | `clipPath` over filled shape, threshold at world y about 728 |
| V1-A34 | 63.58 | 64.83 | 30 | T1 | "I put together this doc" | Pages 1-9 at about 4-frame stagger; each 3-4 f opacity + blur; title line 1 f1528-f1534, line 2 f1540-f1546 | Stagger |
| V1-A35 | 71.77 | 73.00 | 30 | T1 | "Comment story, and I'll send" | Pages at about 3-frame stagger, title line 1 f1725, line 2 f1731 | Same as A34, faster |
| V1-A36 | 2.79 | 2.83 | 1 | T2 | "wrong" | Punch x1.19, step | Scale switch at f67 |
| V1-A37 | 55.125 | 55.17 | 1 | T2 | "middle" | Punch x1.185, step | Scale switch at f1323 |
| V1-A38 | 22.5 | 24.71 | 53 | T2 | "The modern story arc doesn't start out at zero." | x1.04 at 23.5, x1.117 end | `Easing.in(quad)` |
| V1-A39 | 61.17 | 63.54 | 57 | T2 | "Now, if you want to improve" | x1.096 end (ECC) | Same |
| V1-A40 | 67.58 | 71.71 | 99 | T2 | "It's kind of like a cheat sheet" | x1.08 end, gap metric | Same |

---

## 12 Gaps and unknowns

Scene log covers every frame, 0-1775, with no gap. All 74 seconds were inspected in bursts: 24 fps for 0-6, 11.25-14.25, 20.25-21.75, 42.75-44.25; 12 fps for most of the rest; 6.5 fps for 6-11.5 and 6 fps for 30.75-36.75 (so those two windows were not seen at source fps by eye; the 6-11.5 camera and label timing relies on per-frame numeric tracking).

Known limits:
- Exact fonts: INFERRED only. No glyph overlay test was run.
- Full-screen shot scale: ECC failed or gave unreliable results for 11.42, 18.96, 22.5-24.67 (full range), 32.08, 44.46 and 67.58. The gap metric (background feature distance) was used instead, so "locked" for 11.42, 18.96, 44.46 and the end values of 22.5 and 67.58 are estimates; 32.08 stays UNVERIFIED.
- Traditional camera fits use only 3 inliers, because title blobs interfere. Translate values are good to about +-5 px.
- The modern base fit included one false blob (the rotated y label); it did not affect the inlier count materially. S rows with 7 inliers are the reliable ones.
- Bezier fits were run on scale or single-axis progress with an end frame chosen by eye; the 59.6 fit is invalid (control point out of range) and is listed as ease-out only.
- The meme shot: no reliable sub-pixel zoom measure. UNKNOWN whether a tiny push exists.
- A very quiet SFX in the vocals stem cannot be excluded. SFX type names are guesses from spectrograms; nothing was matched to a library.
- 57.68 hit type: UNKNOWN.
- Matte tool, source camera, render tool, and whether UI was built in After Effects or code: UNKNOWN.
- Speech pause cleanup: UNKNOWN. 232 wpm suggests tightening, not proven.
