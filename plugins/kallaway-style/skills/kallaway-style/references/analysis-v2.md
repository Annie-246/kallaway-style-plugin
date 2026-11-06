# v2 editing analysis: "The Ultimate Scriptwriting Format"

Evidence tags: **[V]** VERIFIED (cited as `v2 mm:ss.xx` or frame `fN`; f = t x 25), **[I]** INFERRED, **[U]** UNKNOWN. All px are on the 1080x1920 master. 970 video frames (38.80 s), audio 38.85 s.

Coverage: every frame range was viewed; full list of inspection density in section 12.

## 1 Summary

- [V] A 12-scene explainer with two layouts only: **split** (graphics on top, speaker cutout in a rounded panel at the bottom, 27.36 s = 70.5%) and **full** (speaker full frame, caption only, 11.49 s = 29.5%).
- [V] One object carries the whole video: a glowing "Video Script" card whose colour-coded rows fill in as the speaker names them. The card is the script format, so the graphic is the argument, not decoration.
- [V] Cut rate: 7 layout cuts = 10.8/min; adding 3 hard graphic swaps = 15.5/min; adding 1 animated whip = 17.0/min of visual state changes. Mean scene 3.23 s, longest 9.76 s (S05), shortest 0.68 s (S02).
- [V] Speaker framing never punches in. Both framings are static across the video; all perceived energy comes from the graphics layer, with one exception (31 px pan, A31).
- [V] 113 caption chunks, 1.30 words per chunk, median 6 frames, centered at 67% height, hard-switched with no animation.
- [V] Sound: sub-bass booms on graphic scene entries only, pops on chips, and music rising about 17 dB from section one to the end, never ducked.

## 2 Story structure against visuals

| Beat | Time | Script function | Visual answer | Evidence |
|---|---|---|---|---|
| Promise | 0.00-2.32 | Names the thing | Full finished card builds in 0.72 s, shows the payoff before the explanation | S01 |
| Proof flash | 2.32-3.00 | "short form video" | Six real reels, category proof in 0.68 s | S02 |
| Reset to empty | 3.00-5.72 | "First..." | Card is emptied to grey rows, so the viewer now wants to see it refilled | S03 |
| Aside | 5.72-9.64 | Insider note on lock-in zone | Cut to face, no graphics, authority moment | S04 |
| List | 9.64-19.40 | Seven remaining sections | Card fills row by row, single unbroken scene | S05 |
| Direct address | 19.40-21.60 | "If you don't know..." | Face, eye contact | S06 |
| Applicability | 21.60-25.60 | Works for all, gets all results | Card moves aside, chips list claims left then right | S07 |
| Proof | 25.60-27.48 | "billions of views myself" | Own profile, grid scrolled at speed | S08 |
| Link back | 27.48-29.60 | "this one script writing structure alone" | Physical line ties the wall to the card, then red scan on the card | S09 |
| Lead-magnet ask | 29.60-32.24 | "comment scripts" | Face, stacked keyword caption | S10 |
| Offer shown | 32.24-36.12 | "tactical doc" | Actual doc pages shown | S11 |
| Close | 36.12-38.85 | "hold attention way better" | Face, hard end | S12 |

[I] The structure alternates "show the system" (split) with "talk as a person" (full). Each full segment is the speaker stepping out of the list to comment on it. The empty-card reset at 3.00 is the key narrative device: it converts a finished deliverable into an open loop that is only closed at 18.3 s.

Scene lengths (s): S01 2.32, S02 0.68, S03 2.72, S04 3.92, S05 9.76, S06 2.20, S07 4.00, S08 1.88, S09 2.12, S10 2.64, S11 3.88, S12 2.73.

## 3 Scene types

### Common split layout (S01-03, 05, 07-09, 11)
[V measured f440, f562, f875]
- Background: near-black `#0B0B0B` (corners `#080808`-`#0B0B0B`) with a dot grid, vertical pitch 36 px (3.3% W), dots about 3 px, max luma about 50. Horizontal pitch looks equal but FFT was inconclusive [I].
- Title zone: y 104-222 (5.4%-11.6%), centered.
- Graphics zone: y 250-1140 (13%-59%).
- Caption: y 1267-1305 cap band, center 67.0%.
- Speaker panel: x 71-1008 (6.6%-93.3%, 937 px wide = 86.8% W), top y 1408 (73.3%), bleeds off the bottom edge (no bottom margin, only top corners visible), corner radius about 40 px (3.7% W).
- Speaker is a cutout over the panel: cap breaks the top edge up to about y 1330, raised arm breaks the right edge out to x 1080 (f15, f562). Panel shows a wide framing; KITH logo is 31 px wide in panel versus 99 px full frame, ratio 3.2.
- Z-order [V, f15 "Format" sits over the blurred hand]: bg, card/panel, speaker cutout, then title/caption on top.

**Remotion**: `<AbsoluteFill bg/> <DotGrid/> <Graphics/> <Panel video style={{top:1408,left:71,width:937,borderRadius:'40px 40px 0 0',overflow:'hidden'}}/> <video matted full-size cutout, same transform as panel/> <Title/> <Caption/>`. Render the matte in advance (a transparent WebM or per-frame PNG sequence), then align it to the panel plate.

### T1 Script card (S01, S03, S05, S07, S09)
[V] Card aspect H/W = 1.237. At w=707 (f440, bbox x 187-894, y 258-1133):
- Fill: pure black `#000000`-`#0D0B0B` inside; radius about 18 px (2.5% of card W).
- Stroke: about 4 px, core `#E2F9FF`/`#FBFCE7` (near white, slightly cool). Outer bloom falls off: `#3F322B` at 5 px, `#1E1E1E` at 18 px, `#111111` at 58 px, background by about 110 px.
- Header "Video Script": serif italic, width 203 px (28.7% of card W), y 294-344, center x of card.
- Square markers: 36x36 px (5.1% of card W), x 231-267, joined by a 2 px white dashed spine.
- Row labels: bold sans, cap height 21 px (3% of card W), white, starting x 288.
- Bars: 14 px thick, row pitch inside a block 24-26 px; right edge jitter, left aligned at x 288, right limit x 858.
- Colours: Hook/Rehook red `#A80000`, Lock-in yellow `#E7E606`, Body purple `#8F00A4`, Optional body cyan `#16F1DE`, Closing light grey `#D6D8D3`, CTA green `#30DF09` (marker `#20C305`).
- Empty state (S03): 24 or more grey rows `#978F89` of 9-10 px at pitch 20 px, filling the body. Filled sections replace the top grey rows; the grey block's top edge drops as sections are added (a black band with soft top reveals beneath).

Hero variant (S01): same card, smaller (w 496->574), no labels, 21 bars of 15 px at pitch 19 px in 7 colour groups of 3 bars. Bars staggered so the right edge forms a diagonal while building.

**Remotion**: a `<ScriptCard>` component with `rows[{label,color,bars:[widths]}]`, `revealFrames`, `baseWidth`. Scale the entire card with `transform:scale()` so text and stroke scale too. Stroke `box-shadow: 0 0 0 2px #E8F6FF, 0 0 18px #ffffff40, 0 0 60px #ffffff18`.

### T2 Reel wall (S02)
[V f73] Six 9:16 reel tiles, 3 columns x 2 rows: columns 187-390, 441-644, 695-896, rows 289-638, 684-1033. Tile 200x350 px, gaps 50 px horizontal and 46 px vertical, thin grey outline. Title remains. Tiles flicker in in reading order (A06).

### T3 Chip list (S07)
[V f562, f635]
- Left chip: bleeds off left edge, right edge about 40 px from card left (moves with the card), height 77 px, fill gradient `#2C2C2D`->`#212121`, yellow tab `#F3F717` 28 px wide on the right, 4 px radius, centered text white bold cap 24 px.
- Right chip: x 685-964 (279 px), height 76 px, pitch 108 px (y 509, 617, 725), red tab 24 px on left, same fill, text cap about 30 px, soft drop shadow.
- Card in this scene: w 531, y 329-985, x center goes 540->786->387.

### T4 Profile/grid in frame (S08)
[V] Same glowing frame with warm bloom, aspect 1.25, w 453->526, y top 280 once settled. Contents: a tall screenshot of an Instagram profile plus reels grid, scrolled. The account shown is the speaker's own (handle visible on the profile, 25.80).

### T5 Document pages (S11)
[V f875] Five white pages `#FFFFFF`, no card frame, 3 on top, 2 below centered. Final: row 1 x 140-385, 417-662, 694-939; row 2 x 280-525, 557-802; y 303-653 and 680-1029. Page 245x350. Gaps 32 px horizontal, 27 px vertical. Yellow highlight `#F0F645` on last page footer is part of the doc. Text is unreadable by design but real.

### T6 Full speaker (S04, S06, S10, S12)
[V] Full frame video, caption at the same y as in split layout. Framing static; strip edge in the background stays at x=58 for S04, S06, S10 and the first 9 frames of S12. Shallow depth of field with bokeh, warm key on face, cool practicals behind.

## 4 Typography

- [I] Sans: closest match Inter Tight / Inter Display Bold (double-storey a, single-storey g, flat terminals, flagged 1) with strong negative tracking, about -3% to -4% (letters touch in "CTA", "Works"). Not provable from letterforms; Neue Haas family is the alternative.
- [I] Serif italic: closest match Instrument Serif Italic (condensed, high contrast, swash-like w, F). Neither candidate was installed, so no overlay comparison was done.
- [V] Sizes:

| Element | Measure | % H | Estimated font-size |
|---|---|---|---|
| Caption | cap height 38 px (f440) | 2.0% | ~52 px [I] |
| Title bold (2 lines) | cap ~46 px; line pitch 56 px | 2.4% | ~64 px [I] |
| Title serif italic | width 683, height 61 with descender | 3.2% | ~72 px [I] |
| Caption serif (Scripts) | taller than sans, ~80 px | - | ~80 px [I] |
| Left chip | cap 24 px | 1.25% | ~33 px [I] |
| Right chip | cap ~30 px | 1.6% | ~40 px [I] |

- [V] Colour white `#FFFFFF`, no outline on caption. Title and caption have a faint soft dark shadow, visible only over bright items [I].
- [V] Serif is reserved for the named thing: "Ultimate Scriptwriting Format" (caption f9, title f75) and "Script(s)" (caption f779, title in S11), plus the card header. Sans carries everything else.
- [V] Case: titles Title Case, captions follow speech case except named items (Hook, Body block 1, Rehook 1, CTA).

## 5 Colour

- [V] Base: `#0B0B0B` and pure black inside frames. White is the only text colour.
- [V] Single brand accent: red `#AC0001`-`#AB0001` for the title highlight, matching the row red `#A80000`.
- [V] Row palette above. Tabs: yellow `#F3F717`, red.
- [I] Why: a black stage with saturated data colours is an editor-UI/terminal look that signals "system". Six hues map to six section types, so colour is the legend: red rows are hooks (Hook, Rehook 1, Rehook 2 all share it), purple rows are body blocks, so the pattern of hook/body alternation is readable with no text. "Optional" gets the cooler cyan and neutral grey, visually less essential; green for CTA is "go".
- [I] Why yellow on the first-claim chips and red on the outcome chips: yellow ties to "lock-in", attention; red ties to title accent and results.
- [I] The speaker is warm skin on black, so he reads as the only warm natural object against a cold graphic stack.

## 6 Motion and transitions

Fitted cubic-beziers (max error shown), from per-frame bbox tracking [V for the data, I for the curve identity]:

| Move | Frames | Bezier fit | Err |
|---|---|---|---|
| Card zoom S01 w 496->574 | f18-50 | (0.25,0.1,0.15,1) | 3.4% |
| Card zoom S03 w 590->669 | f110-140 | (0.40,0,0.15,1) | 1.5% |
| Frame zoom S08 w 453->526 | f648-680 | (0.25,0,0.15,1) | 3.4% |
| Pages zoom S11 w 682->798 | f831-866 | (0.30,0,0.05,1) | 2.1% |
| Slow drift S05 w 590->717 | f248-484 | (0.05,0,0.65,1) | 1.0% |
| Card x right 525->786 | f547-588 | (0.30,0.8,0.80,1) | 1.0% |
| Card x left 786->387 | f589-634 | (0.30,0.1,0.15,1) | 2.1% |
| Card rise cy 834->724 | f75-109 | (0.05,0.8,0.95,1) | 2.1% |
| Hero title highlight | f1-23 | (0.25,0,0.05,1) | 2.1% |
| Italic title highlight | f76-85 | (0.25,0.4,0.55,1) | 0.5% |

House rule: **a zoom is one 30-34 frame, 1.13x-1.17x hit, sharply fast-in with a long tail** (about 50% of the distance in the first 25% of time). Use `Easing.bezier(0.3,0,0.15,1)` for all zooms and the leftward card slide.

Transitions by type [V]:
- Hard cut, layout change: f143, f241, f485, f540, f740, f806, f903. No flash, no whip, no zoom through.
- Hard graphic swap inside split: f58, f75, f640. Bottom third stays continuous.
- Animated: only S08->S09 whip (A25).
- Entrance signature: on every return to split the card starts low (cy 834) and rises with a long ease-out, while the title re-wipes.
- Exit signature: when one graphic replaces another in split, the old one accelerates upward for 5-6 frames (47 px in f52-57; same at f635-639) then is hard-replaced, so the swap reads as a throw. S11 and S05 have no exit because they are cut to full.

## 7 Caption system

[V] Chunk stats: 113 chunks, 147 caption words (transcript has 151 tokens plus an unrecognised "Now"), 1.30 words/chunk. Duration median 6 f (0.24 s), mean 8.6 f, min 2 f, max 41 f.
- Position: centered x=540, cap band y 1267-1305. Identical in split and full, so the eye does not move across a layout cut.
- Appearance: hard swap on one frame, no fade, pop or scale (verified at 25 fps at 06.08, 30.04, 31.16). No active word highlighting.
- Sync: within about +/-2 frames of word onset (`comment` f768 = word 30.72).
- Over the speaker in both layouts (f15, f790).
- Chunking rule: function words go alone or paired ("is the", "you go", "and a", "Now to"), and named terms stay whole ("Body block 1", "lock-in zone.", "those sections", "you must do").
- Punctuation kept as spoken: commas and periods shown ("video,", "about.", "leads.").
- Numbers rendered as digits: "2 to 3" (06.52), "the 3", "to 5" (33.80).
- Rewording: "Optional closing" drops nothing but "Aligned lead magnet." capitalises a mid-sentence phrase as a label. "with" is skipped at 30.04, an editorial trim.
- **Stack mode**, one occurrence (S10): "comment" f768 holds, line 2 serif "Scripts" adds f779, line 3 rolls "and I" f788, "will" f793, "send" f797, "you a" f802. Line pitch about 77 px, top line stays anchored at caption y. Only the action keyword stays on screen. [I] Used only here because it is the instruction the viewer must remember.
- Long holds occur when the row and caption duplicate: "Rehook 1" 27 f, "Optional body block 3" 37 f, and these are the moments the speaker pauses.
- Serif chunk "Ultimate Scriptwriting Format" 41 f covers 11 spoken-word positions, and it is the only time text outruns speech.

Timing table (start frame, a few +/-1 from 12.5 fps views): This 0, is the 4, Ultimate Scriptwriting Format 9, for 50, short 57, form 62, video, 69, First 75, you 81, start 84, with 90, the Hook, 92, then 103, you go 109, into 116, the 122, lock-in zone. 125, Very 143, underrated 152, 2 to 3 163, sentences 174, that 183, come 186, right 192, after 200, the hook 207, that 215, nobody 219, talks 227, about. 234, Then 241, you've 245, got 250, Body block 1 255, Rehook 1 281, Body block 2 308, Rehook 2 334, Optional body block 3 363, Optional closing 400, and a 430, CTA 436, with 448, an 455, Aligned lead magnet. 459, If you 485, don't know 492, how to 498, write 503, scripts, 507, just 517, follow 523, this. 531, It 540, works 544, for 549, every 552, niche, 560, every type 567, of 578, content 580, It'll 590, get 595, you 599, views, 603, followers, 612, and 624, leads. 631, I've 638, literally 644, done 653, billions 659, of 670, views 673, myself 679, on 692, this 698, one 704, script 711, writing 718, structure 724, alone. 734, Now to 740, help 744, you 748, this 751, even 756, more 760, comment 768, "Scripts" 779, and I 788, will 793, send 797, you a 802, tactical 806, doc 827, breaking 833, down 841, the 3 845, to 5 853, things 864, for 871, each 877, of 881, those sections 884, you must do 903, in 923, your 926, scripts 930, to 939, hold 942, attention 948, way 959, better. 964.

## 8 Asset treatment

- [V] Speaker: matted cutout on top of the same footage plate. A cyan rim from the set light survives on the sleeve (f15). Matte edge is clean with hand blur retained.
- [V] Reels (S02), profile (S08), docs (S11): raw real screenshots, no colour grade, no blur, no tilt. Frame stroke and bloom come from the card system for wall/profile; pages stay naked white.
- [V] Docs are real content at a size that is unreadable, so they prove volume, not detail. Highlight on last page is left in.
- [I] Scroll asset is one long stitched image at least 11,000 px tall scaled to card width. In practice, a tall grid image can be replaced by a long composite; motion is too fast to read the tiles.
- [V] No stock, icons, emoji, logos or sticker elements appear.
- [V] Graphics are not motion-blurred at any speed, including scroll peak and whip (f670, f693). Scroll stays sharp; only speaker footage has real blur.

## 9 Sound and music

Method: htdemucs stems, 20 ms band energy, spectrograms. Stem separation leaves vocal bleed, so only events strongly above the local floor are listed.

[V] Levels: vocals overall -17.5 dBFS RMS, median -20 dB; no_vocals overall -30.9 dB.

| Time | Music floor (no_vocals median) |
|---|---|
| 4-10 s | -48 to -50 dB |
| 12 s | -46 dB |
| 14 s | -42 dB |
| 16-18 s | -38.5 dB |
| 20 s | -35 dB |
| 22 s | -32.5 dB |
| 24-38 s | -30.6 to -32.4 dB, flat |

[V] Speech-to-music gap therefore narrows from 28 dB to 11 dB. No ducking is visible: the floor does not dip with speech or rise in gaps. Plucked arpeggio around 300-800 Hz runs from 0.0 s, bass layer enters at 11.6 s, melody line near 1 kHz enters at about 17 s. Music runs to the last frame with no fade or final hit. Tempo estimate 117.5 BPM [I].

[I] The rise is staged across the list, so energy grows as the card fills, and it plateaus at the moment the claims start at 22 s.

SFX list [V time and class; I type name]:

| Peak | Band | Type guess | Hits |
|---|---|---|---|
| 0.20 (0.10-0.42) | sub 40-60 Hz, -15 dB | sub boom | Video start, card flicker |
| 1.25-1.76 | tonal 2.4-12 kHz, sharp stop | tonal riser/shimmer | Rising under held card, cut off before rumble |
| 1.80-2.40 | low rumble | sub swell | Card held, leads to swap |
| 2.48 | sub, -14 dB | sub boom | Wall tiles flicker (f58 = 2.32, +0.16) |
| 3.20 (3.08-3.38) | sub, -15 dB | sub boom | Reset to empty card (f75 = 3.00, +0.20) |
| 9.84 (9.70-10.14) | sub, -17 dB | sub boom | Return to card (f241 = 9.64, +0.20) |
| 21.90 | sub, -24.5 dB | soft sub | Card flicker (f540 = 21.60, +0.30) |
| 22.18 | down-chirp 1.5k->150 Hz | pop | Chip 1 (22.04, +0.14) |
| 22.86 | same, loudest | pop | Chip 2 (22.72, +0.14) |
| 24.26 | same | pop | Views + ripple (24.12, +0.14) |
| 24.58 | same | pop | Followers (24.44, +0.14) |
| 25.14 | same | pop | Leads (25.00, +0.14) |
| 24.80-25.38 | tonal, same as 1.25 riser | tonal riser | Before profile swap |
| 25.68 | sub, -18 dB | sub boom | Profile (f640 = 25.60, +0.08) |
| 27.90 (27.76-28.10) | low-mid swell, -23 dB | soft whoosh | Whip (A25) peak |
| 32.52 (32.40-32.60) | rising sweep into sub, -15.5 dB | riser + boom | Doc pages (f806 = 32.24, +0.28) |

Observed rules [V]: booms mark graphic scene entries; cuts to full speaker are silent (f143, f485, f740, f903); row reveals in S05 are silent, so the list relies on music and speech; the SFX peak follows the visual by 0.08-0.30 s (booms have slow attack; audio onset is closer to visual). Pops are constant +0.14 s from chip start, so align the sample so the transient falls 3-4 frames after the chip begins.

## 10 Placement decision rules

1. **When the speaker enumerates named parts, a persistent diagram fills row by row and stays on screen.** Evidence: 03.28-18.12. Counterexample: "2 to 3 sentences" at 06.5 has no graphic because it is an aside.
2. **When the row's name is about to be spoken, the row starts before the word.** Lead: Hook 0.46 s (label 03.24 vs word 03.74), Lock-in 0.24, Body 1 0.14, Rehook 1 0.28, Body 2 0.22, Rehook 2 0.28, Optional 3 0.12, Closing 0.18, CTA 0.42 (17.12 vs 17.54). Note: Whisper timestamps have error. Counterexample: none in this video.
3. **When the speaker leaves the list to comment or address the viewer, cut to full.** Evidence: 05.72 "Very underrated", 19.40 "If you don't know", 29.60 "Now to help you", 36.12 "you must do".
4. **Cuts land on the sentence start, 1-3 frames before the first word.** Evidence: 05.72 vs 05.84, 09.64 vs 09.76, 19.40 vs 19.48, 21.60 vs 21.64. Counterexamples: 32.24 and 36.12 both cut mid-sentence, on the object noun ("tactical doc") and on the imperative ("you must do").
5. **When a concrete thing is named, show the real thing as the cut happens.** Evidence: "tactical doc" 32.24, "short form video" 02.32, "billions of views myself" 25.60. Counterexample: "lead magnet" at 18.4 is not shown; the doc is saved for the CTA.
6. **When a claim is a list of categories, give each item a chip on its word.** Evidence: niche 22.04, type of content 22.72, views 24.12, followers 24.44, leads 25.00. Chip side changes with claim type: applicability left, outcomes right.
7. **When "alone/one structure" re-links proof to method, draw the link literally and light the object.** Evidence: connector 27.60-27.88, scan 28.36 on "script". The white line physically ties the reel wall to the card.
8. **When a graphics scene ends with a cut to full, there is no exit move, but a graphic replaced by a graphic gets a thrown exit.** Evidence: 02.24, 25.40 vs 05.68, 19.36.
9. **When the speaker counts on his hand, the card row sits in sync with it, so gestures are not cut around.** Evidence: raised palm in S05 at every row. [I] He gestures toward the card area, and this is why the arm is allowed to break the panel.
10. **When a number is spoken, display digits.** Evidence: 06.52, 33.80, 34.12.
11. **When an action is requested, stack the keyword and hold it.** Evidence: 30.72-32.24. Only instance.
12. **Booms go on graphic entries, never on cuts back to the face.** Evidence: section 9. Counterexample: none.

Why these choices at strong moments [I]:
- **00.00 hero build**: start in motion on the first word, full colour first, to give an instant payoff and stop the scroll; the flicker reads as a screen switching on.
- **03.00 reset**: the colour disappears the instant he says "First", creating the need for completion, and the boom underlines it as a chapter.
- **24.12 red ripple**: the first outcome ("views") is the actual desire, so it gets the only circle effect in the video, one-off rarity creating peak attention.
- **26.1 scroll**: "billions" is too large to state, so distance stands in for magnitude; peak speed sits on the word.
- **28.36 scan**: "this one script" needs the viewer back on the card after scrolling, and a band of light is an attention-return tool that adds no new information.
- **31.16 serif Scripts**: the keyword to type is styled as the brand's serif, so it looks like a quoted command.

## 11 Animation inventory

All [V] for frames; rebuild notes [I]. Bars and labels are in card coordinates.

| ID | Start-end (s) | Frames | Scene | Script line | Keyframes | Rebuild |
|---|---|---|---|---|---|---|
| V2-A01 | 0.00-0.24 | f0-6 | S01 | "This" | Card luma: 11.1, 9.9, 10.3, 13.0, 10.6, 12.6, 16.8 | Opacity flicker table `[.35,.2,.3,.8,.3,.7,1]` |
| V2-A02 | 0.04-0.92 | f1-23 | S01 | "This is the ultimate" | Text left edge 190->156 by f11 (35 px); line 2 starts f7; highlight 3->785 px | Per-char translateX(35->0) + opacity over 11 f, stagger 0.3 f/char; red rect scaleX from left with bezier(.25,0,.05,1) behind text |
| V2-A03 | 0.04-0.72 | f1-18 | S01 | same | Bars sweep left to right top to bottom | Each bar wipes in 8 f, stagger 0.8 f per bar |
| V2-A04 | 0.00-2.00 | f0-50 | S01 | through "format" | Rise cy ~830->713; w 496 until f18, peak speed f24-26, 574 at f50 | translateY long ease-out; scale 1->1.157 per zoom curve |
| V2-A05 | 2.08-2.28 | f52-57 | S01 | "short" | Top 362->315, deltas 2,3,5,8,11,18 | translateY ease-in `t^3`, hard replace at f58 |
| V2-A06 | 2.32-2.80 | f58-70 | S02 | "short form video" | Tile starts: r1c1 f58, r1c2 f60, r2c1 f60-62, r1c3 f61, r2c2 f63, r2c3 f64; settle f70 | Per-tile opacity flicker 3 cycles over 8 f |
| V2-A07 | 3.04-3.40 | f76-85 | S03 | "First" | Red x 180, right 277->897 (10 f), serif chars finish about f95 | Same as A02, shorter |
| V2-A08 | 3.00-4.40 | f75-110 | S03 | "First you start with the" | Top 469->360, w 590 constant | translateY from +110 |
| V2-A09 | 3.24-3.84 | f81-96 | S03 | "the hook" | Label grey fade then white; marker pops; bar sweeps 14 f | Row component: label fade 6 f, flicker once, bar wipe |
| V2-A10 | 4.44-5.60 | f110-140 | S03 | "then you go into" | w 590->669 | Zoom curve |
| V2-A11 | 4.68-5.44 | f117-136 | S03 | "lock-in zone" | Label f117, bars f119-136, bars staggered 5 f with leading bloom | Row with 4 bars, soft glow on leading edge, drop grey block top |
| V2-A12 | 9.64-19.36 | f241-484 | S05 | Whole list | Rise 469->252 top; w 590->717 | Single interpolate, bezier(.05,0,.65,1) |
| V2-A13 | 9.68-10.20 | f242-254 | S05 | "Then you've got" | Title identical to A07 | Re-run A07 on every re-entry |
| V2-A14 | 10.00-10.80 | f250-270 | S05 | "body block one" | Label f250, bars to f270 | Row |
| V2-A15 | 11.20-12.00 | f280-300 | S05 | "re-hook one" | Label f280 | Row |
| V2-A16 | 12.24-13.04 | f306-326 | S05 | "body block two" | Label f306 | Row |
| V2-A17 | 13.36-13.88 | f334-347 | S05 | "re-hook two" | Bars 13 f | Row |
| V2-A18 | 14.40-15.52 | f360-388 | S05 | "optional body block three" | Bars 27 f | Row |
| V2-A19 | 15.96-16.60 | f399-415 | S05 | "optional closing" | White bars, about 16 f | Row |
| V2-A20 | 17.12-18.12 | f428-453 | S05 | "CTA" | Bars f430-453 | Row |
| V2-A21 | 21.64-22.20 | f541-555 | S07 | "It works for" | Flicker luma 23, 26, 18, 35, 31, 19, 42; title left 233->198; red line 2 f544-553 | Full-card flicker, A02 with line-2 highlight |
| V2-A22 | 21.76-23.52 | f544-588 | S07 | "works for every niche" | Card x 525->786 | bezier(.3,.8,.8,1) |
| V2-A23 | 22.04-23.40 | f551-585 | S07 | "every niche / every type" | Chip1 f551, Chip2 f568, 6 f fade, per-char text | Chips parented to card left, gap 37 px |
| V2-A24 | 23.56-24.00 | f589-600 | S07 | "it'll get" | Gap closes to about 7 px, opacity 0 | Translate toward card, fade 10 f |
| V2-A25 | 23.56-25.36 | f589-634 | S07 | "it'll get you views followers" | Card x 786->387, peak 26 px/f at f598 | bezier(.3,.1,.15,1) |
| V2-A26 | 24.12-24.44 | f603-611 | S07 | "views" | Dark-red disc `#760004`->`#400007`, 1 px light rim, center about (940,660), r about 170 by f607 | Scale circle fast out, alpha decays, cut at f612, chip appears through it |
| V2-A27 | 24.12-25.28 | f603-632 | S07 | "views followers leads" | Chips f603, f610, f625, 6 f fade, x settles left | Per-chip tab first then text |
| V2-A28 | 25.40-25.56 | f635-639 | S07 | "leads" | Deltas 3,6,10,16; chips same | A05 |
| V2-A29 | 25.60-27.20 | f640-680 | S08 | "I've literally done" | Rise top 489->280 (f640-650), w 453->526 | Rise then zoom |
| V2-A30 | 26.12-27.64 | f653-691 | S08 | "billions of views myself" | px/f: 16, 43, 73, 112, 157, 211, 275, 349, 414, peak ~470 at f668-673, 427, 390, 377, 347, 320, 296, 273, 253, 235, 217, 202, 187, 174, 161, 150, 139, 128 | Interpolate scrollY by symmetric ease with total 11,400 px |
| V2-A31 | 27.36-28.96 | f684-724 | S09 | "on this one" | dx/f 5,10,16,25,38,55,74,85; then card eases to cx 540; total ~800 px | Wall and card in one row container with a 3 px white glowing line at y 718; bezier ease-in-out |
| V2-A32 | 28.36-29.36 | f709-733 | S09 | "script writing structure alone" | Band enters top f709, reaches bottom f725; red border/glow decays by f733 | Absolute gradient `transparent->#E0002A->transparent` height about 25% card, `mix-blend-mode: screen`, top from -25% to 100% linear over 16 f, then glow fade 8 f |
| V2-A33 | 30.72-32.24 | f768-805 | S10 | "comment scripts and I will send you a" | Line adds at f779, roll f788/793/797/802 | Static stack, hard swap |
| V2-A34 | 32.24-33.04 | f806-826 | S11 | "tactical" | Pages at f806, 807, 808, 809 (4+5). Group top 435, 416, 397, 379, 359, 350, 345, 344, 344, 345, 350, 355, 360, 363, 363, 362, 360, 358, 357 | Stagger 1 f per page; group spring with overshoot of 19 px, about 16 f period |
| V2-A35 | 32.28-33.00 | f807-823 | S11 | "tactical doc" | Title left 203->168, red line 2 f814-823 | A02 |
| V2-A36 | 33.28-34.64 | f832-866 | S11 | "breaking down" | w 682->798 | Zoom curve; note the zoom starts on the word "breaking" |
| V2-A37 | 36.48-37.32 | f912-933 | S12 | "must do in your" | Bg x -31 px; first steps -10, -10, -5 | Digital translateX of the video with ease-out over 21 f |

## 12 Gaps and unknowns

- Inspection density: 25 fps bursts over 0-1.44, 2.0-3.44, 5.48-5.96, 9.4-10.84, 19.28-19.6, 21.48-29.72, 30.56-33.48; 12.5 fps over 3.44-5.48, 10.84-19.4, 33.48-36.3, 36.24-38.85; 10 fps over 5.9-9.4, 19.56-21.6, 29.68-30.56; 1 fps contact sheet only on 1.44-2.0 and 30.56 region was covered by per-frame bbox tracking. Caption starts seen only at 12.5 fps are +/-1 frame.
- [U] Exact font identity (see section 4). Fonts are not installed locally, so overlay was not tested.
- [U] Whether the source has a wider frame than used. Pan A37 needs overscan and the reason for it is unknown; the face did not move toward center, and there may also be a scale change near 2% (one match suggested 0.98 at weak correlation).
- [U] Whether full and panel shots are one 4K take or two angles. Ratio 3.2 fits a 4K reframe [I].
- [U] Matte method. Edge quality implies per-frame rotoscoping or an AI matte.
- [U] Whether tile/row flicker is expression-driven or a preset. Only the pattern was measured.
- [U] Band profile of the scan could not be isolated cleanly, as the band overlaps coloured rows; sizes in A32 are read by eye from f711, f717.
- [U] SFX names are guesses from spectrograms; no listening was possible. Event at 32.08 (hi band) may be vocal bleed, so it is excluded. Small band events under about 28 dB are treated as bleed.
- [U] Whether music is one track or layered edits; the music stem contains the SFX, so the first 3.4 s floor is contaminated.
- [U] Tile internal contents and thumbnails were not transcribed; they are proof texture.
- Whisper errors handled: missed "Now" at 29.6, "you" at 35.94 is early because caption "you must do" starts at 36.12, "senses" = "sentences", caption is the reference.
- [I] Lead values in rule 2 depend on Whisper timing, which has about +/-0.1 s error.
- Frame false positives dropped from cuts.json: f56, f77-81, f219, f242-256, f657-696, f809. Real: f143, f241, f485, f540, f740, f806, f903, with f75 and f640 as graphic swaps; f58 was missed by cuts.json at threshold (reported as f56 card exit).
