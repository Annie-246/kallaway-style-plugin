# v3 editing analysis (3.mp4, 1080x1920, 24 fps, 91.26 s, 2190 frames)

Evidence labels: VERIFIED = seen or measured in v3 at the cited time or frame. INFERRED = reasoned from evidence, not proven. UNKNOWN = could not be determined.
Frame numbers are 0-based, f = t x 24. Pixel values are in the 1080x1920 frame.

## 1 Summary

- VERIFIED: 91.26 s, 317 words, 3.47 words/s (208 wpm).
- VERIFIED: 15 hard cuts (f73, 111, 273, 378, 716, 762, 1137, 1225, 1332, 1430, 1516, 1617, 1713, 1813, 1892) = 9.9 cuts/min, mean shot 5.7 s. A 16th layout change at f2027 swaps the whole stage while the PiP continues. f1813 was absent from cuts.json. All other cuts.json entries are false positives (hand motion, stage motion, keyframe pulses every 72 frames), except f662, f682, f694, which are clip swaps inside a card, and f6, f1018, which are elements appearing.
- VERIFIED: 28 logged scenes (18.4 per minute). 8 are full-frame talking head (27.3 s, 29.9%). The other 20 share one continuous diagram stage (70.1%).
- VERIFIED: one take. The PiP background shows no jump in any composite section. No transition effect exists anywhere: every cut is a hard cut, and the motion lives inside the stage.
- Core idea (INFERRED): the video is one diagram that keeps evolving. A timeline becomes a tree, the tree grows by a node per content type, and each node opens into a real example. The speaker returns to full screen for verdicts. Music is removed only on three punch-ins.

## 2 Story structure against visuals

| Time | Story beat | Visual | Reason (INFERRED) |
|---|---|---|---|
| 0.00-3.04 | Hook claim | Light wall of 6 viral reels with view counts | Proof before explanation. Light is unique in the video, so the cut to dark at 3.04 is the largest visual change (diff 119 vs 40-57 elsewhere) |
| 3.04-4.63 | Name the thing | Punch-in, music off, serif name at chest | The term gets silence and a type change |
| 4.63-11.38 | History, two types | Timeline scroll, 2-node tree, 2 profiles | Abstract history gets a map |
| 11.38-15.75 | Verdict on old era | Face | Opinion belongs to the person |
| 15.75-29.83 | Third type | Timeline reprise, third node, reel, hero card, serif notes | Same map, one node more |
| 29.83-31.75 | Consequence | Punch-in, music off | Pivot line |
| 31.75-47.38 | 2026 split | New title, 2026, AI clip, 3 blurred categories, Eduslop card | Blur creates a list to complete |
| 47.38-51.04 | Eduslop verdict | Face | "complete junk food" |
| 51.04-55.50 | Tactical | Carousel | Slide between nodes makes the list physical |
| 55.50-59.58 | Tactical verdict | Face | |
| 59.58-63.17 | Application | Carousel, red dot, pill sheen | Payoff node gets the extra marks |
| 63.17-67.38 | Definition | Face | |
| 67.38-71.38 | Examples | 4-step card slide | One card per format |
| 71.38-78.83 | Prove it / who it is for | Face, then punch-in, music off | Addresses the buyer directly |
| 78.83-84.46 | Recommendation | Full tree, keep set turns green | Decision on the same map |
| 84.46-91.26 | CTA | Doc grid and red banner | Deliverable shown as volume |

## 3 Scene types

Shared base layers. Stage background `#060606`-`#090909` (VERIFIED, f144, f1980). Dot grid: dots peak about `#181818`, pitch about 18 px horizontally (measured 18.3 px; vertical pitch not cleanly measured, INFERRED equal).
PiP window (VERIFIED f48, f2130): x 68-1011, y 1404-1920, 943 x 516 px (87.3% W, 26.9% H), bleeds off the bottom, top corners radius about 48 px.
Person cutout: the speaker is matted over the window, so hat and hand rise above y 1404. Hat top y about 1325. The cutout layer ends at a flat line at y about 1225: fingertips are visibly clipped flat there (VERIFIED, f797, f970). The hand overlaps stage content (card corner, f797).
Rebuild: `<PiPVideo/>` rounded rect plus a second copy of the same video with a matte, clipped at y 1225, above the stage. Remotion needs a pre-rendered alpha or matte video.

### 3.1 HOOK_WALL_LIGHT (0-3.04)
- Background `#E1E1E0`, dots `#D6D6D6` pitch about 11.5 px, plus a faint square line grid in the lower middle (VERIFIED f48; cell size about 60 px, INFERRED).
- Title 2 lines centred, bbox x 205-876, y 133-236, black `#000000`; "Crazy Viral" in serif italic.
- Tiles 226 x 366 px, columns x 147 / 427 / 707 (gap 54), rows y 293-660 and 778-1143, small radius about 5 px. All 6 play video.
- View pills 172 x 53 at y 677 and 1154: bg `#094707`, text and eye icon `#26FF17`, bold about 40 px.
- Caption black, bbox y 1257-1296.
- Timing: tiles start f0, 2, 3, 4, 5, 6 in reading order, each blur plus opacity to sharp in about 6 frames, with an upward settle. Pills at f23, 25, 28, 30, 33, 35 (stagger 2.4 f), 4 f fade from pale to full green.
- Why (INFERRED): six proofs fill the frame on "new type of content"; pills land on "that is starting" so numbers arrive as the claim rises. Green reads as growth and is reused at the end as "keep".

### 3.2 TH_FULL and TH_PUNCH
- Static hard cut from composite, no zoom during the shot (VERIFIED, f275 vs f376 scale 1.00).
- Word caption at chest: bbox y about 1186-1248, centre about 1212 (63%).
- Framing varies slightly by shot, relative to f300: f1137 shot 1.00; f1332 and f1516 shots about 2% wider; f1713 shot about 4% tighter (VERIFIED, background template match, plus or minus 1%).
- TH_PUNCH (f73, f716, f1813): about 11% tighter than base. Starts about 10-13% wider than its settled scale, reaches settled in about 10 frames with ease-out, then locks. Music off in all three.
- Why (INFERRED): the zoom marks a statement; the silence removes all competition.
- Remotion: `scale = interpolate(f,[0,10],[1.0,1.11],{easing:Easing.bezier(.2,.7,.2,1)})`, then hold. Set base transform-origin near the face.
- Serif statement variant (f73-111 only): white serif italic at chest y about 61%, "Application" fades in f82-86, "Content" appended about f103. Word captions stop for that line.

### 3.3 TIMELINE
- Centre title (3.5.1 Typography section 4), line, dots, ticks, years.
- Spacing 563 px between years. Dot outer diameter 45 px at this zoom, fill `#AE0001`, white ring 4-5 px. Line white about 3 px, y 746 at entry.
- Major tick about 343 px tall, minor tick at midpoint about 225 px, both thin grey.
- Year labels white, bold, digit height about 65 px, centred above each dot about 240 px.
- Move: 1603 px left in 46 f (f112-158), cubic-bezier(.8,.05,.14,.95), peak 166 px/f at f133. Motion blur horizontal, visibly multi-sample at peak (VERIFIED 5.33-5.75).
- Why (INFERRED): dates are spoken while the numbers run; the scroll carries time passing without any new asset.
- Remotion: one `<div>` translateX, render with frame blending or `<Trail layers={5} lagInFrames={.2}>`.

### 3.4 TREE
- f252: pills 188 x 58 px at y 857-915, x 302-490 and 619-807, radius about 14, border 3 px `#858585`, fill `#000000`, text white bold about 24 px.
- Elbow stems white 5 px to a horizontal at y 975. Dot (551, 975), red 32 px, outer about 42 px.
- Year bbox x 442-658, y 1036-1105.
- Build: tree falls from y 600 to y 764 (dot) in 22 f with fast ease-out, starting about 6.71 on "roughly". Bezier (.1,.1,.18,.8). Timeline fades out under it f165-176.
- Stems and pills appear in order: dot, stem spreading sideways, pills fade up f168-178 (VERIFIED 7.04-7.42).
- Node insertion (f434-447): right pill slides out to open a centre slot, new pill scales in from small (18.17-18.5).
- Why (INFERRED): the fork literally shows "two sides"; red dot marks the "you are here" point, carried from timeline to tree so the viewer never loses the anchor.

### 3.5 PROFILE CARDS (8.29, 9.54)
- 292 x 436 px, radius about 16, near-black fill, 2 px grey stroke, x 195-487 and 593-885, y about 349-784.
- Avatar 72 px with ring, serif italic handle, tab icons, 3 x 2 thumbnails about 80 x 115.
- Blur-fade in, 6 f. Stage eases down 173 px in 34 f to make room (bezier about .3,0,.1,1).
- Thumbnails in the second card are his own reels; a tile animates (f258+), probably screen capture (INFERRED).

### 3.6 CARD_HERO and CARD_NOTES
- Border white 2 px, radius about 18, video inside, glass creator pill at bottom (avatar, Inter @handle, serif italic "1.3M Followers").
- Width 263 px at f540, 626 at f600, 632 at f620 (x2.4); height 572 to 965 (VERIFIED by edge tracking).
- At f640-700: moves left and shrinks to width about 570, right notes column appears at x about 687-1020, serif italic white about 44 px, line pitch about 46 px.
- Notes reveal word by word in sync: "Amazing" 27.25, "at" 27.5, "building" 27.75, "authority" 27.9, "Tough" 28.5, "to" 28.75, "scale" 29.08. Each word fades over about 5 f from about 30% grey.
- Inside the card, clips swap on f662, f682, f694: cut points in the reel sit inside the note sequence.
- Why (INFERRED): the card demonstrates storytelling while its clips cut; the serif notes are the editor's quiet commentary, separate from the spoken caption.

### 3.7 TIMELINE_CLIP (33.0-35.6)
Landscape card about 480 x 280 px under the timeline, white 3 px border, radius about 12, fades from dark in 8 f. Clip: AI footage of boxes unpacking. Stage rises 160 px to make room (f771-829).
Why (INFERRED): "AI content and copy culture" needs a recognisable AI look, not a diagram.

### 3.8 TREE_REVEAL (37.6-41.9)
Pills 3-wide with labels under Gaussian blur, border sharp. Each label sharpens on its word (VERIFIED):
| Label | Unblur | Word start |
|---|---|---|
| Application | f934-940 | 39.02 |
| Tactical Edu. | f966-972 | 40.26 |
| Eduslop | f998-1004 | 41.58 |
Why (INFERRED): an open list. The blur creates a slot the viewer waits to see filled.
Remotion: `filter: blur(interpolate(f,[w,w+6],[8,0]))` on the label only.

### 3.9 CAROUSEL (51.04, 59.58)
- No title. Zoomed stage. f1272: card x 265-794, y 118-873; pill x 331-750, y 963-1092; line y 1226, about 7 px white.
- f1460: card x about 810-1252 minus offset, y 168-834, pill y 911-1027, line and dot y 1142, dot height 62 px.
- Slide: 758 px in 37 f (bezier .25,0,.02,1), peak 74 px/f at f1231. 670 px in 48 f (.25,.4,.1,.95). Strong horizontal blur on cards (VERIFIED 51.25-51.42).
- Neighbour card stays visible at the right edge at reduced size in frame, about 45 px.
- Application pill sheen f1458-1470: bright gradient sweep across the pill left to right on "newest" (VERIFIED 60.81-61.12).
- Why (INFERRED): the viewer physically travels along the same tree, so each category is a place.

### 3.10 EXAMPLE_CAROUSEL (67.38-71.38)
- Cards about 468 x 668 px, y 277-945, gap about 77 px, pitch 545 px. Labels above, bold about 44 px white, y about 240.
- Application pill anchored at y about 1045, static.
- 4 slides of about 545 px: starts f1634, f1650, f1665, f1685, each about 12-16 f, motion blur on cards and labels.
- Incoming card and label dim, then fade to full; the leaving label blurs.
| Slide | Start | Word | Word start |
|---|---|---|---|
| to Scenarios | 68.08 | scenarios | 67.98 |
| to Case Studies | 68.75 | case | 68.82 |
| to Hypotheticals | 69.38 | hypotheticals | 69.58 |
| to Live Builds | 70.21 | live | 70.56 |
Slide leads the word by up to 0.35 s (VERIFIED).

### 3.11 TREE_RECAP (78.83-84.46)
- 5 pills small, dot size 20 px at f1892.
- Green pills: fill `#055D0B`, border lighter, white text. Turn at f1919-1921: Tactical Edu. first, then Storytelling and Application, on "these".
- Zoom: dot 20 px (f1912) to 34 px (f1962), then back to 21 px (f2002); outer pills leave frame during zoom-in.
- Grey-out: Entertainment and Eduslop keep black fill and dim further at about 83.25 (VERIFIED 83.25-83.83).
- Why (INFERRED): "do not waste your time with entertainment or eduslop" is a decision, so the map itself is recoloured.

### 3.12 CTA_DOC_GRID
- Tree and title vanish at f2027 with no fade; PiP continues.
- Doc size 158 x 204 px. Columns x 182, 368, 554, 740; rows y 322, 548, 780, 1000; last row x 368, 554. 14 docs white with red and blue text.
- One doc starts every 2 frames in reading order, each from dark grey to white in about 5 f (f2027 to about f2056).
- "Comment" fades up at f2030, "Format" at f2038, banner fades in at f2041 with slow rise; stage settles upward about 88 px by about f2040-2050.
- Banner red `#AC0001`, about 655 px wide, radius about 6.
- Why (INFERRED): 14 pages show the size of the reward and match "the doc" in the red bar. Red links to the dot, the video's single accent.

## 4 Typography

| Role | Font (closest match) | Status | Size | Colour | Other |
|---|---|---|---|---|---|
| Title | Inter Display or Inter Tight Bold | INFERRED, no reference font available on this machine | about 50 px (2.6% H), line pitch 54 px | white or `#000000` | tracking about -3%, Title Case, centred |
| Title accent | Instrument Serif Italic | INFERRED, high-contrast condensed italic | about 56 px optical match | same | one word per title |
| Caption | same sans Bold | INFERRED | about 52 px (2.7% H) | `#FFFFFF` or `#000000` | no stroke or shadow visible, sentence case, keeps punctuation |
| Year | same sans Bold/ExtraBold | INFERRED | digit height 65-69 px, about 90-95 px | `#FFFFFF` | |
| Pill | same sans Bold | INFERRED | about 24 px at tree zoom | white | |
| Notes, handle | serif italic | INFERRED | about 44 px | white | |

- Title positions: dark bbox x 244-836, y 115-206 (6.0%-10.7%); hook y 133-236 (VERIFIED). Lateral margin at least 19%.
- Title text per section: "This New Type Of Content / Is Going Crazy Viral Right Now"; "This Is How Social Media / Used To Look Like Before"; "This Is How AI Changed / Social Media Forever"; "These Formats Will Change / Social Media Forever"; "Comment "Format" / To Get The Doc" (VERIFIED).

## 5 Colour

| Item | Hex | Evidence |
|---|---|---|
| Dark stage | `#060606`-`#090909` | f144, f1980 |
| Dark dots | about `#181818` | f144 |
| Light stage | `#E1E1E0` | f48 |
| Light dots | `#D6D6D6` | f48 |
| Accent red | `#AE0001` dot, `#AC0001` banner | f252, f2130 |
| Pill border | `#858585` | f252 |
| View pill | `#094707` bg, `#26FF17` text | f48 |
| Node green | `#055D0B`, text white | f1980 |

Logic (INFERRED): near-black with white text lets real footage supply all saturation. Red means "here, this one". Green means "works" (views, keep). Red is the only accent until the green payoff. Warm room footage in the PiP keeps the dark stage from going cold.

## 6 Motion and transitions

- No dissolves, wipes or flashes (VERIFIED). Every hard cut into composite lands on a stage already moving or on a title reveal, which hides the cut (f378, f1225, f1430).
- House ease: strong ease-out with soft start. Fits (VERIFIED by tracked positions, mean error under 0.011 unless noted):

| Move | Frames | Distance | Peak | Bezier fit |
|---|---|---|---|---|
| Timeline scroll | f112-158 | 1603 px | 166 px/f | (.8,.05,.14,.95) |
| Timeline 2026 | f762-804 | 930 px | 92 px/f | (.35,.05,.02,1) |
| Carousel 51 s | f1225-1262 | 758 px | 74 px/f | (.25,0,.02,1) |
| Carousel 59.6 s | f1430-1478 | 670 px | 50 px/f | (.25,.4,.1,.95) |
| Tree drop | f160-182 | 192 px | 19 px/f | (.1,.1,.18,.8) |
| Stage down 19 s | f456-490 | 215 px | 17 px/f | (.35,0,.14,.95) |
| Stage move 42 s | f1003-1030 | 336 px | 23 px/f | (.4,0,.42,.8) |

- Default for a rebuild: `Easing.bezier(.3,0,.1,1)` over 30-40 frames.
- Every major element enters by blur plus opacity plus small shift. Motion blur on all fast moves.
- The stage rarely stops: slow drift continues between moves; dots keep shifting 2 px/f after a drop (f186-195).

### Title reveal (each new section entry: f0, 111, 378, 762, 1892)
- Line 1 word-by-word, a new word every 1.5 f, each from about 50% opacity, about 5 px above, settling in 4 f.
- Line 2 enters as a block: 42 px below, rising with ease-out over 12 f, with flicker (f111-121 approximate opacity .75, .6, .65, .4, 1, .6, .75, 1, .7, .95, 1).
- Line 1 sinks about 7 px, so the lines close together.
- Replays on every return, even for the same title at f378.

## 7 Caption system

- One word per screen, short pairs merged ("was a", "is where", "want to", "you're a", "it would", "in the", "that you") (VERIFIED). Mean 1.0x words per screen; 317 words, about 310 caption changes measured.
- Timing: switch within about 2 frames of Whisper word start (median -0.4 f, p10 -1.9, p90 +1.9). Previous word holds until the next one, no gaps. Median 6 frames on screen, p10 3, p90 13.
- Instant swap: no fade, pop or scale (VERIFIED, 8.25-11.0, 76.8-77.5).
- Position fixed centre x 540. Composite: y 1250-1300, 66.5%. TH: y about 1212, 63%.
- Digits for numbers ("3"). "two" rendered as "2." at 22.2 (VERIFIED).
- Title and caption never overlap; caption sits in a reserved 1240-1320 band above the hat.
- Hand can pass beside caption; hand over caption z-order is UNKNOWN.

## 8 Asset treatment

- Real reels and screen captures, always inside a rounded card with a thin white or grey border, always playing (VERIFIED 19.4-29.8, 42.4-47.4, 51-55.5, 59.6-63.2, 67.4-71.4).
- Burned subtitles left in. Third-party face in the Eduslop card is blurred (VERIFIED 42.4+); this is the negative example.
- Own reels shown with their own embedded PiP (f1272).
- Creator credit pill added on third-party footage (@omgadrian).
- Generated AI clip for the "AI content" beat (INFERRED from the look).
- Green view pills and "13.7M Views" establish proof.

## 9 Sound and music

- Music: one loop, 130 BPM, period 7.385 s (4 bars), starts at 0.00, runs to the end with no fade (VERIFIED by autocorrelation and spectrogram). Track identity UNKNOWN. Melodic plucks over bass.
- Levels: voice about -21.5 dB RMS, music about -33 dB RMS, so -12 dB relative (VERIFIED, stem RMS). No ducking: bass median 14.0 dB in voice gaps vs 13.6 dB under voice (VERIFIED).

### Music dropouts
| Riser start | Music off | Music on | Cut at off | Cut at on |
|---|---|---|---|---|
| 2.44 | 3.08 | 4.71 | 3.042 | 4.625 |
| 29.15 | 29.87 | 31.76 | 29.833 | 31.750 |
| 74.57 | 75.55 | 78.87 | 75.542 | 78.833 |

Music stops within 2 frames of each punch-in and returns at the next cut (0 to 2 frames after, except 4.71 at +2). The return lands on a bass entry. During off sections stems show only room-level residue (-59 to -66 dB) at two of three; 3.1-4.6 shows -41 dB of speech bleed.

### Sound events (no_vocals stem)
| ID | Time | Type guess | Event |
|---|---|---|---|
| S1 | 2.44-3.10 | tonal riser, harmonic comb to 16 kHz | Into cut f73 |
| S2 | 6.29-6.74 | soft whoosh | Stage tilt, tree drop |
| S3 | 16.93-17.29 | soft whoosh | Tree entry f415 |
| S4 | 19.29-19.58 | soft whoosh | Reel card entry |
| S5 | 21.53-21.90 | soft whoosh | Arcs on "blend" |
| S6 | 22.90-23.44 | soft whoosh | Card scale-up |
| S7 | 27.29-27.93 | soft whoosh | Card left, notes begin |
| S8 | 29.15-29.93 | tonal riser | Into cut f716 |
| S9 | 32.98-33.25 | soft whoosh | AI clip |
| S10 | 35.14-35.83 | soft whoosh | Tree over timeline |
| S11 | 37.62-37.94 | soft whoosh | Re-frame to 3 nodes |
| S12 | 42.48-42.85 | soft whoosh | Eduslop card |
| S13 | 51.05-51.25 | soft whoosh | Carousel slide |
| S14 | 59.65-60.12 | soft whoosh | Carousel slide |
| S15 | 60.73-61.10 | soft whoosh | Sheen or dot (INFERRED) |
| S16-S19 | 67.9-68.4, 68.82-69.10, 69.37-69.85, 70.30-70.61 | soft whooshes | One per card slide |
| S20 | 74.57-75.55 | tonal riser | Into f1813 |

Type guesses are INFERRED: whooshes appear as low-mid triangular swells (about 300-1500 Hz). No click on captions and no SFX on pills, docs or the f2027 swap were detected (VERIFIED absence at stem level, subject to Demucs residue).

## 10 Placement decision rules

1. When the speaker names or restates the core thesis, the editor punches in to full face and removes music until the next cut. Evidence: 3.04 "It's called application content", 29.83 "So most personal brands stick to education", 75.54 "If you're a business owner". Counterexample: 63.17 "Application is when..." is the definition, full face, music stays, no zoom.
2. When the speaker gives a date or era, the editor shows the timeline and scrolls to it. Evidence: 4.63 "From 2021", 15.75 "In 2024", 31.75 "in 2026". Counterexample: 78.83 no date, no timeline.
3. When a new category is named, the editor adds a node or moves to it, unblurring the label on the word. Evidence: 39.02, 40.26, 41.58; 19.0 for Storytelling. Counterexample: 8.48 "Entertainment" pills appear about 1.3 s before the words at 7.04.
4. When the speaker explains what something is, the editor shows a real example card. Evidence: 19.4, 42.4, 51.1, 59.7.
5. When the speaker judges something, the editor returns to the face. Evidence: 11.38 "You could pretty much make any type", 47.38 "This is complete junk food", 55.50 "These are still very effective". Counterexample: 28.4 "but it's very tough to scale" stays on the card, using serif notes.
6. When the speaker lists items, the editor makes one visual move per item. Evidence: 67.98-70.56 four slides; 39.02-41.58 three unblurs. Counterexample: doc grid list "scenarios..." none.
7. When a pro and con are stated, the editor writes them in serif beside the asset. Evidence: 27.25-29.48. Only instance.
8. When the speaker recommends a choice, the editor recolours the map. Evidence: 80.0 green on "these".
9. When the speaker says the CTA word, the editor swaps the stage on that word. Evidence: f2027 (84.46) vs "Comment" 84.42.
10. When any stage move happens, the editor lays one whoosh on it, only if the move is a section or layout change. Evidence: S2-S19. Counterexample: Timeline scrolls at 4.63 and 31.75 have no separate whoosh (music re-entry covers them).
11. When a shot would show graphics for more than about 8 s, the editor returns to the face. Evidence: shots of composite 8.3, 6.75, 15.5?? See exception: f378-716 is 14.08 s and f762-1137 is 15.62 s, both without a face. This rule is therefore rejected; those sections hold attention through internal beats every 1-2 s.

## 11 Animation inventory

| ID | Start-End | Frames | Scene | Script line | Keyframes | Rebuild |
|---|---|---|---|---|---|---|
| V3-A01 | 0.00-0.25 | f0-6 + 6 | Hook | "There's a new type" | tile starts f0,2,3,4,5,6 | Stagger 1.2 f, blur 12 to 0, opacity 0 to 1, y 20 to 0 |
| V3-A02 | 0.00-0.50 | f0-12 | Hook | same | see title reveal | `<TitleReveal/>` |
| V3-A03 | 0.96-1.50 | f23-40 | Hook | "that is starting" | pills f23,25,28,30,33,35 | Stagger 2.4 f, opacity 4 f |
| V3-A04 | 3.04-3.46 | f73-83 | Punch | "It's called" | scale start 1.0, settled f83 | Spring-free ease-out to 1.11 |
| V3-A05 | 3.46-4.40 | f83-105 | Punch | "application content" | "Application" f83-90, "Content" f103 | Serif word fades |
| V3-A06 | 4.63-5.13 | f111-122 | Timeline | "From 2021" | title reveal | `<TitleReveal/>` |
| V3-A07 | 4.67-6.58 | f112-158 | Timeline | "from 2021 to 2024" | peak f133 | translateX, blur trail |
| V3-A08 | 5.75-6.75 | f138-165 | Timeline | "Social media" | y 746 to 985 | translateY |
| V3-A09 | 6.71-7.58 | f161-182 | Tree | "roughly looked" | dot 600 to 750 | Tree group |
| V3-A10 | 7.00-7.42 | f168-178 | Tree | "looked" | pills fade, stems extend | scaleX on line from dot |
| V3-A11 | 8.08-9.50 | f194-228 | Tree | "entertainment content" | down 173 px, card f199 | Stage y; card blur-fade |
| V3-A12 | 9.54-9.83 | f229-236 | Tree | "education content" | card fade | Same |
| V3-A13 | 15.75-16.79 | f378-403 | Reprise | "In 2024" | title, scroll 357 px | Enter mid-move |
| V3-A14 | 17.29-18.10 | f415-434 | Tree 3 | "third content type" | rise 130 px, spreading | Stage y |
| V3-A15 | 18.08-18.50 | f434-444 | Tree 3 | "that really" | Educational slides; Storytelling scales in | Slot insert |
| V3-A16 | 19.00-20.42 | f456-490 | Tree 3 | "storytelling content" | card 19.38, poster 19.75 | Stage down, card blur-fade |
| V3-A17 | 21.25-22.25 | f510-534 | Tree 3 | "perfect blend of the" | arcs from pills f510, meet f530 | Stroke-dash on 2 white arcs, tapered |
| V3-A18 | 22.75-25.00 | f546-600 | Card hero | "Entertaining stories" | w 263 to 626, tree out f545-560 | Scale x2.4 over 54 f |
| V3-A19 | 26.67-27.58 | f640-662 | Notes | "content is amazing" | width 632 to 586, x -100 | Slide and scale |
| V3-A20 | 27.25-29.08 | f654-698 | Notes | "Amazing at building authority, but it's very tough to scale" | words at 27.25, 27.5, 27.75, 27.9, 28.5, 28.75, 29.08 | Per-word fade |
| V3-A21 | 29.83-30.25 | f716-726 | Punch | "So most" | zoom 10 f | V3-A04 |
| V3-A22 | 31.75-33.50 | f762-804 | Timeline | "Well in 2026" | title, 930 px | Same as A07 |
| V3-A23 | 33.00-33.33 | f792-800 | Clip | "AI content" | opacity | Fade card |
| V3-A24 | 35.33-35.67 | f848-860 | Clip | "education" | card out | Fade |
| V3-A25 | 35.50-37.67 | f852-904 | Tree | "content has now split again" | tree fade, timeline fade by f904 | Crossfade inside stage |
| V3-A26 | 37.50-38.25 | f900-918 | Tree | "There's three" | dot and pills move left, zoom | Stage scale |
| V3-A27 | 39.00-41.75 | f934-1004 | Tree | "application... edu-slop" | unblur 3 labels | Per-label blur |
| V3-A28 | 41.79-43.00 | f1003-1030 | Pan | "edu-slop" | 336 px down, 158+ px left, card f1018 | Stage move |
| V3-A29 | 43.58-44.75 | f1046-1074 | Hero | "just says words" | tree fade f1055-1062, card 465 to 595 | Scale, fade |
| V3-A30 | 51.04-52.58 | f1225-1262 | Carousel | "Tactical education" | peak f1231 | translateX, blur |
| V3-A31 | 59.58-61.58 | f1430-1478 | Carousel | "But application content" | dot visible f1436 | Same |
| V3-A32 | 60.81-61.12 | f1458-1467 | Carousel | "newest category" | sheen left to right | Gradient mask translate |
| V3-A33 | 68.08-71.00 | f1634-1697 | Examples | "scenarios... live builds" | starts f1634,1650,1665,1685 | 4 steps, 545 px |
| V3-A34 | 75.54-75.96 | f1813-1823 | Punch | "If you're a" | zoom 10 f | V3-A04 |
| V3-A35 | 78.83-79.33 | f1892-1904 | Recap | "you want to" | title reveal | `<TitleReveal/>` |
| V3-A36 | 79.96-80.04 | f1919-1921 | Recap | "these" | fill black to green | Color swap 2 f |
| V3-A37 | 79.67-81.75 | f1912-1962 | Recap | "across these three buckets" | dot 20 to 34 px | Stage scale 1.7 |
| V3-A38 | 81.98-83.33 | f1975-2000 | Recap | "Do not waste your time" | scale 34 to 21 | Reverse |
| V3-A39 | 84.46-85.71 | f2027-2056 | CTA | "Comment, format" | 14 docs, 2 f stagger | Doc grid |
| V3-A40 | 84.58-85.00 | f2030-2041 | CTA | "Comment" | title words, banner | Fade and rise |

Times for A10, A14-A15, A17, A19, A23-A26, A29 are from 12 fps viewing, so plus or minus 1 frame. Keyframes for A37-A38 are from dot size samples every 10 frames.

## 12 Gaps and unknowns

- Viewed at source fps: 0-6, 15.7-18, 51-55.6, 67.3-71.8, 75.3-77.5, 78.7-81, 84.4-86.6. Viewed at 12-16 fps: 8.15-11.5, 18-31.45, 31.7-45.2, 59.5-63.25, 81-84.4. Viewed at 6 fps: 86.65-91.26.
- 1 fps only, plus frame-difference analysis: 11.5-15.7, 31.45-31.7, 45.2-47.4, 47.4-51, 55.6-59.5, 63.25-67.3, 71.8-75.3, 77.5-78.7. No stage events occur in these per the difference data; 1090 to 1137 shows card hold.
- Fonts are INFERRED, no reference fonts on this machine for overlay.
- Exact music track and exact SFX files UNKNOWN. Whoosh classification is from a stem with Demucs bleed; quiet SFX may be missed, and whooshes may be part of the music in a few cases.
- Zoom estimates in punch-ins are plus or minus 2% because of motion and low background contrast. Scale curve shape is INFERRED.
- Dot grid vertical pitch, grid line cell size, tile hook upward travel and blur radii are estimates.
- Whether the cutout is a roto matte or chroma source is UNKNOWN; only the result is seen.
- Caption vs cutout z-order UNKNOWN (no overlap observed).
