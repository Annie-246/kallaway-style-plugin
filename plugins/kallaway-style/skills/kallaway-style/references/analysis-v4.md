# v4 reverse-engineering analysis

Source: `4.mp4`, 1080x1920, 24 fps, 89.83 s, 2156 frames. Times are seconds, frame numbers are 0-based at 24 fps.
Evidence labels: VERIFIED = seen or measured, cited as v4 + timecode. INFERRED = reasoned from evidence. UNKNOWN = not determinable from this file.

## 1 Summary

v4 is an educational short built as a continuous "explainer stage": a near-black dot-grid canvas above a cut-out speaker, broken by locked full-screen talking-head blocks.

- 18 scenes, 17 layout boundaries, average scene 5.0 s. The felt pace is faster because the graphic zone changes state roughly every 1.5-2.5 s. VERIFIED (scene_log.csv); the 1.5-2.5 s figure is INFERRED from the animation inventory.
- Screen time: split layout 73 percent (65.6 s), full-screen head 27 percent (24.2 s, five blocks of 1.88, 2.67, 6.58, 5.38, 7.75 s). VERIFIED.
- Cut rate: 17 layout boundaries = 11.4 per minute. With about 9 embedded cuts inside reference clips (19.58, 20.75, 23.21, 30.42, 31.62, 32.71, 34.08, 36.04, about 38.3) = 17.4 per minute. VERIFIED, except 36.04 and 38.3 which are the least certain.
- cuts.json lists 37 candidates. Only 9 are full-layout hard cuts: 3.292, 5.167, 10.417, 13.083, 43.042, 49.625, 70.083, 75.458, 82.083. VERIFIED by frame burst. The other 8 layout boundaries are in-stage swaps or moves. The rest of cuts.json is embedded clip cuts, flicker or animation.

Signature techniques:
1. Cut-out speaker over a rounded panel, head and arms breaking the panel edges (v4 9.0, 35.0, 50.0).
2. One 6-frame flicker-on envelope used on many elements (section 6), and one eased dock move.
3. Literal visual metaphors that animate on the exact word: brain draining as "decay", hawk scan and dive into a cone that becomes the story model, with audio that follows (pitch falls on decay, sound drops out on the dive).

## 2 Story structure against visuals

| Time | Beat | Script job | Visual treatment |
|---|---|---|---|
| 0-3.29 | Hook | Promise | Title, arrow to a blurred answer, then proof wall of 5 phone clips |
| 3.29-5.17 | Name | Reveal the term | Full-screen face, term set in serif italic caption |
| 5.17-10.42 | Problem | Why retention falls | Retention chart draws, unknown viewer with red question mark |
| 10.42-13.08 | Solution | Need | Full-screen face |
| 13.08-18.25 | Roadmap | Two hacks | Tiles 1 and 2 under parent bracket, focus moves to 1, tile becomes chapter icon |
| 18.25-25.54 | Tip 1 | Principle and consequence | Clip plus link/waveform, then brain decay |
| 25.54-39.5 | Tip 1 proof | Example | Frozen preview, then real clip with original audio, speaker reacts |
| 39.5-43.04 | Proof recap | Claim | 3x3 evidence grid |
| 43.04-49.62 | Depth | Why it works | Full-screen face |
| 49.62-54.96 | Tip 2 | Transition | Tile 2 recall, same title, tile becomes hawk-eye icon |
| 54.96-61 | Tip 2 metaphor | Hawk hunts | Hawk scan, lock, dive, impact |
| 61-70.08 | Tip 2 model | Broad to deep | Ring to cone, labels setup context and point |
| 70.08-75.46 | Warning | Common mistake | Full-screen face in silence |
| 75.46-82.08 | CTA | Offer | Brain turns green among thumbnails, Comment banner, 9 doc pages |
| 82.08-89.83 | Close | Value of doc | Full-screen face, ends cold |

Pattern: graphics carry the "what", the full-screen face carries the "so what" and moments of trust. INFERRED from the table.

## 3 Scene types seen

Coordinates are px at 1080x1920, then percent. VERIFIED by measurement on the cited frames unless marked. Remotion notes assume a 1080x1920 composition at 24 fps.

### 3.0 Split layout base (all graphic scenes)
- Canvas: `#030303` with dot grid, pitch about 15.5 px, dots up to `#3B3B3B` (v4 9.0). A soft grey radial glow sits behind labels, background rises to about `#1B1B1B` near glowing text (v4 35.0).
- Graphic zone: y 0 to about 1195 (62 percent). Caption band centre y 1262 (65.7 percent). Panel top y 1398 (72.8 percent).
- Panel: x 67-1010 (87.3 percent wide, 6.2 percent side margin), runs off the bottom edge, top corner radius about 33 px, no stroke.
- Speaker: person cut-out on top of the panel, not clipped by it. Cap rises to about y 1310, 88 px above the panel. Hands and arms exit the panel at top and sides (v4 23.0, 50.0, 64.0). Matte edge is soft with a visible halo (v4 35.0).
- Panel background is static (mean difference about 1 grey level across v4 9.0, 35.0, 62.5, 80.4) and looks sharper than the full-screen background. INFERRED: a separate room plate with the person rotoscoped over it. True wide shot or generated plate is UNKNOWN.
- Rebuild: `<AbsoluteFill>` stack: canvas PNG; panel `<div>` with `overflow:hidden` holding plate; `<OffthreadVideo>` of alpha-matted speaker above it with no clipping; caption; graphics.

### 3.1 Full-screen talking head (S02, S04, S11, S15, S18)
- Locked camera. SIFT on background gives scale 0.999-1.001 and under 1 px shift between first and last frames of all five blocks. VERIFIED. No punch-in.
- Face is about 2.7-3.0x the panel size. INFERRED, weak SIFT fit (5-7 inliers).
- Caption centre y 1232 (64.2 percent), 30 px higher than split.
- Only the caption on screen. Enter and exit by hard cut.

### 3.2 Chapter tile (S05, S12)
- Dark glass square, fill `#494948` at centre, corner radius about 14 percent, thin light rim. A bright sheen travels round the rim (v4 13.4-14.5, 50.0-51.5).
- Tile about 360 px (33 percent W) when alone. Pair of tiles about 260 px growing to about 305 px (13.2-16.2 slow push-in).
- Numerals in serif italic white.
- Icon changes by cross flicker in 4-5 frames (v4 17.21-17.42, 51.83-51.96).
- Dock move: tile, icon and label go to header. Tile final x 487-593 (106 px), y 123-229. Label final y 252-315, x 272-807 for Visual Alignment. Icon shrinks less than tile: about 137 to 60 px against about 367 to 106 px.
- Rebuild: one `<Tile>` with a `state` prop, driven by `interpolate(frame,[f0,f0+36],[0,1],{easing:Easing.bezier(.48,0,0,1)})`.

### 3.3 Title block
- Two centred lines, y 170-285, x 176-902 at widest (67 percent W). White `#FFFFFF`, faint red underglow on the hook title only.
- Words enter one at a time, 2-5 frames apart. Line 2 enters as one unit midway through line 1 (v4 5.58, 13.42, 50.04).
- Rebuilt identically in S12 as a callback.

### 3.4 Retention chart (S03)
- Axis box x 237-862, y 376-650. Gridlines at 100, 50, 0 about `#555555`. Labels 100%, 50%, 0, 0:00, 0:30 in light grey.
- Curve `#CB0F09`, about 6 px, faint red glow. End dot red with white ring, about 26 px, lands about 7.9.
- Rebuild: SVG path with `strokeDashoffset`, dot pop at path end.

### 3.5 Unknown viewer avatar (S03)
- Circle diameter about 264 px at centre (540, 950). Fill `#191919`, ring `#B20007` about 7 px, silhouette `#EDEDED`, red `?`.
- Silhouette brightens 7.44-8.0, `?` fades in 8.11-8.45.

### 3.6 Clip window (S06, S09)
- First form x 101-978, height about 508, radius about 30 px, 2 px white stroke, white outer glow (v4 20.8).
- Second form x 124-956, y 477-943, 832x466 (v4 35.0).
- Clips are muted when the speaker talks over them (S06) and play with audio when they are the subject (S09).

### 3.7 Progress bar (S09)
- Outer x 146-932, y 999-1088, thin white top and bottom rules with thick end caps, inner fill `#FDFDFD`, empty `#303030`.
- Fill starts x 170 at about 27.54, linear at 2.59 px per frame (62.2 px/s), full about 39.5. Duration matches the 12 s clip. VERIFIED 27.92-39.17.

### 3.8 Brain (S07, S16)
- Wireframe rotating brain with glow, centre about (540, 800), width about 250 px in S07.
- Fill level drops and hue changes: green 23.25, yellow-green 24.0, yellow 24.3, orange 24.67, red from 24.75. Colour order reverses in S16.
- INFERRED: pre-rendered 3D loop with a fill mask, or a video asset with a hue ramp.

### 3.9 Evidence grid (S10) and doc grid (S17)
- S10: 3x3, tile about 223x148 px, row tops 511, 719, 927. Tiles enter every 3 frames in reading order, 39.50-40.50.
- S17: 3x3, tile 260x187 px, columns 110, 410, 710, rows 439, 677, 915. Gap 40x51 px. Tiles enter every 2 frames, 77.50-78.17, grey then white.
- S17 sweep: saturated green wave in reading order with a fading tail, 79.50-80.25. Exact hex not sampled.

### 3.10 Hawk, ring and cone (S13, S14)
Sections 6 and 11 hold timings. White hawk silhouette with white glow. Horizon arc thin lilac. Beam pivots on hawk. Red trail has pink core `#D54452` family with red glow. Cone white stroke about 5 px with outer lip. Beam fill `#D80006` with lighter core.

### 3.11 CTA header (S17)
- Line 1 "Comment" bold plus "Story" serif italic in curly quotes, y 200-287.
- Banner about x 264-815, y 302-360, red `#AC0003` to `#C50311`, small radius, white bold text.

## 4 Typography

- Bold face: tight neo-grotesque, heavy weight, negative tracking, letters nearly touching (v4 9.0 "understanding"). INFERRED closest match Inter Display/Inter Tight ExtraBold, tracking about -4 percent. Not proven by letterforms.
- Accent face: narrow high-contrast serif italic (v4 3.0 "Storytelling Hack", 15.5 "Maxing", 80.0 "Story"). INFERRED closest match Instrument Serif Italic.
- Mixing rule: the idea word goes in serif italic inside a bold line (Storytelling Hack, Videos, Maxing, Hawk Eye, Story). VERIFIED.
- Title: cap height about 46 px (2.4 percent H), em about 63 px (3.3 percent H), line pitch about 57 px (about 0.9).
- Chapter label: em about 72 px at header, width 535 px. Em is INFERRED from the measured box.
- Caption: em about 57 px (3.0 percent H). Em INFERRED from ascender height.
- Case: Title Case on titles, spoken case on captions, lower case on diagram labels ("setup context", "point").

## 5 Colour

| Role | Hex | Evidence |
|---|---|---|
| Canvas | `#030303` | v4 9.0 |
| Dots | up to `#3B3B3B` | v4 9.0 |
| Text | `#FFFFFF` | v4 9.0 |
| Tile | `#494948` | v4 35.0 |
| Curve red | `#CB0F09` | v4 9.0 |
| Ring and `?` red | `#B20007` | v4 9.0 |
| Banner red | `#AC0003` to `#C50311` | v4 80.0 |
| Cone red | `#D80006` | v4 67.0 |
| Ring pink core | `#D54452` | v4 60.0 |
| Bar fill / empty | `#FDFDFD` / `#303030` | v4 35.0 |
| Brain green-yellow sample | `#9AD807` (mid transition) | v4 24.0 |

Rule: white for structure, red for problem and focus, green only for healthy comprehension and the doc sweep. INFERRED. Why: on near-black, one accent keeps the eye on one place, and red/green read as bad/good without a label.

## 6 Motion and transitions

### F1 Flicker-on (signature)
Brightness normalised to final, per frame, measured on numeral (v4 13.5), label (17.25), clip (19.33), bar (27.42):
`[0.3, 0.7, 0.5, 0.25, 0.65, 1.0]` over 6 frames (0.25 s). VERIFIED on those four. Title line 2 at 5.58 and "Best" at 0.08 are similar but noisier.
Remotion: `const FL=[.3,.7,.5,.25,.65,1]; const o = frame-f0<0 ? 0 : frame-f0<6 ? FL[frame-f0] : 1;`

### F2 Word entry
Opacity via F1 or short fade, Gaussian blur about 8 to 0 px, y from about -20 px to 0 over about 8 frames. VERIFIED visually at 5.25-5.5. Blur value INFERRED.

### F3 Dock move
Tracked label bottom edge 18.17-19.58 fits `cubic-bezier(0.48, 0, 0, 1)` over 36 frames, start frame 436, rms error 0.0003. VERIFIED fit. Vertical motion blur near peak 18.46-18.6. Second instance 52.58-54.9 looks the same shape with a longer tail, not fitted.

### F4 Stage pan
Chart and title pan left 524 px, 5.17-7.67. Remaining distance decays exponentially, tau about 10.7 frames. VERIFIED. Chart lift of 319 px, 6.5-9.0, reaches 55 percent at 7.42. Lift starts before "because" so the avatar has room.

### F5 Zoom-through dissolve
22.5-23.25: clip width 882, 905 (22.75), 943 (22.92), 977 (23.0), past 1080 (23.17). Opacity dip 23.04-23.12, brain visible beneath at 23.17. VERIFIED.

### F6 Other
- Slow push-in on tiles 13.1-16.2, about 17 percent.
- Boundaries to full screen are hard cuts with no flash, zoom or whip. The hook title fades 2 frames before the 3.292 cut, the only such case. VERIFIED.
- Hard cuts land just before a sentence: 3.29 (`It's` 3.38), 5.17 (`The` 5.20), 10.42 (`What` 10.46), 13.08 (`So` 13.12), 43.04 (`And` 43.08), 49.62 (`Now` 49.62), 70.08 (`Too` 70.20), 75.46 (`Now` 75.52), 82.08 (`These` 82.14). Cut leads speech by 0-3 frames. VERIFIED.

## 7 Caption system

- One word per screen, sometimes two short words ("are the", "at a", "Look at"). About 241 caption states for 307 words, 1.27 words per screen. Detection is approximate.
- Median duration 8 frames, p10 4, p90 14, longest held on sentence ends.
- Onset median -0.008 s from Whisper word start, p10 -0.05, p90 +0.04. Effectively frame-exact. VERIFIED.
- No animation, no highlight, no box, no stroke. Hard on and off. Exception: key term fades in 3 frames (3.83-3.96).
- Keeps punctuation ("rate.", "$500,000.").
- Runs over everything, including clip speech in S09.
- Style switch: "Comprehension Maxing" in serif italic only at the term reveal (3.8-5.1). Later uses are bold (v4 12.3, 49.3). VERIFIED.
- Spelling differs from Whisper ("Mr.Beast" at 26.5). VERIFIED.
- Rebuild: map words to `<Sequence>` by frame, merge a very short word with its neighbour.

## 8 Asset treatment

- Short-form thumbnails: playing video, 9:16, soft glow in their own colour, no stroke (v4 2.6, 75.8).
- Reference clips: window with white stroke and glow, colour unaltered. VERIFIED.
- Freeze preview: frame of next clip with feathered red edges and no window, then crisp window at 27.42 (v4 25.6-27.4).
- 3D brain: INFERRED pre-rendered.
- Docs: real page screenshots, with one yellow highlighted line on the last page.
- Icons: flat white on tile with blur glow.
- Speaker matte: full body to panel, soft edge, no outline or shadow.

## 9 Sound and music

Levels are RMS dBFS. Mix peak 0.0 dBFS. VERIFIED from stems.

| Segment | Mix | Voice | Non-voice |
|---|---|---|---|
| 0-3.3 | -18.7 | -20.3 | -28.1 |
| 3.3-13.1 | about -20 | about -20.7 | -36 to -42 |
| 13.1-23.2 | about -19 | about -21 | -25 to -27 |
| 23.2-25.5 | -18.1 | -23.6 | -20.0 |
| 27.5-39.5 clip | -24.4 | -27.7 | -28.5 |
| 39.5-49.6 | -19 to -22 | -19.6 to -23 | -34 |
| 52.8-66 | -16.7 | -18.8 | -22 |
| 70-75.45 | -19.4 | -19.8 | -53.5 |
| 75.45-89.8 | -20 to -22 | -20 to -22 | -40 |

Music states (timing VERIFIED in spectrogram, instrument INFERRED):
- 0-13.7: faint plucks. May include voice leakage, share UNKNOWN.
- 13.8-14.8: silent (-58 dB).
- 15-25.5: tonal sound design, not a loop.
- 26.4-27.4: near silent before the clip.
- 27.5-39.46: clip audio only, VO removed.
- 39.5-52: sustained chord loop, phrase about 3.7 s, sharp entry at 39.5, dip 42.8-43.3 at the full-screen cut.
- 53.4-68.6: wind/drone bed, rises, dropout 59.2-60.0, ends 68.7.
- 68.7-75.5: silence.
- 75.6-89.8: same type of loop at about -40, entries 75.6, 79.0, 82.7, 86.4, with gaps before each.

Music sits 12-19 dB under voice. No ducking seen: chord bands stay flat across words 40-49 s. INFERRED from spectrogram.

Sound effects (level = 10 ms peak in no_vocals, type INFERRED, timing VERIFIED):

| Time | Type | Peak dB | Event |
|---|---|---|---|
| 0.25-0.60 | sub boom | -21 | Red disc pop, Best |
| 2.10-2.45 | riser/whoosh, bright | -13 | Last tile lands, "educational" |
| 5.30-5.50 | sub whoosh | -25 | Chart enters on hard cut |
| 7.10-7.30 | sub whoosh | -25 | Chart lift, avatar coming |
| 8.95 | soft tick | -29 | Unclear |
| 13.07-13.35 | sub hit | -21 | Hard cut to roadmap |
| 14.90-16.0 | upward tonal sweep | -11 | Bracket and term, "Comprehension" 15.02 |
| 16.47-16.70 | whoosh | -19 | Stage pan to tile 1 |
| 17.45-17.70 | bright impact | -12 | Icon and label, "visual" |
| 18.56 | whoosh | -21 | Dock move peak |
| 19.45-19.60 | hit | -13 | Clip flicker-in |
| 21.7-23.3 | low drone build | -28 | Zoom-through |
| 23.38-25.5 | falling tonal glide | -13 start | Brain decay |
| 51.98-52.20 | impact | -10 | Logo on "hawk" |
| 53.6 | whoosh | -16 | Dock move 2 |
| 60.15 | impact | -10 | Hawk reaches dot |
| 63.89 | swell | -12 | Cone fill starts |

Rule: SFX mark graphic state changes, not cuts to the face. VERIFIED: no SFX event on 3.29, 10.42, 43.04, 70.08, 82.08. The cuts into graphics at 5.17 and 13.08 do have one, which supports the rule that the sound belongs to the graphic. Counterexample: the cuts into graphics at 49.62 and 75.46 have none.

## 10 Placement decision rules

1. When the speaker names a new concept, the editor sets it in serif italic. Evidence 3.83 caption, 14.83 label, 52.08 Hawk Eye. Counterexample: "Visual Alignment" 17.2 is bold only.
2. When the speaker makes an abstract claim about the viewer, the editor shows a diagram of the metric. Evidence 5.17 chart, 23.25 brain.
3. When the speaker gives the need or the reasoning, the editor cuts to full-screen face. Evidence 10.42, 43.04, 70.08. Counterexample: 39.5-43 the claim stays on the grid.
4. When the speaker lists items, the editor numbers them first, then shows only one. Evidence 13.2 two tiles, 16.3 tile 2 leaves.
5. When the speaker starts an item, the editor turns its tile into an icon and docks it as a persistent header. Evidence 17.2-19.6, 51.8-54.9.
6. When the speaker says a verb of change, the graphic does that change. Evidence "decay" 24.24 brain drain, "dive" 59.24 dive, "narrow" 59.84 fall to point.
7. When the speaker cites an example, the editor previews it frozen, then lets the clip speak while the speaker looks at it. Evidence 25.54-27.42, about 26.9-39.5.
8. When the clip is long, the editor adds a progress bar. Evidence 27.42-39.5. Purpose INFERRED.
9. When the speaker says "every", the editor shows a grid of many. Evidence 39.52 word, 39.5 grid.
10. When the speaker gives a warning, the editor removes all sound but voice. Evidence 68.7-75.5. Counterexample: 10.4-13 is also near silent and is not a warning.
11. When the CTA word is said, the word appears. Evidence "comment" 77.60, on screen 77.58.
12. When the hook promises a secret, the editor shows it blurred. Evidence 0-1.5. The term is named at 3.76. Whether the blurred text is that term is INFERRED from its two-line shape.
13. Graphic labels may lead speech. Evidence "setup context" on screen 66.16, spoken 67.28. Counterexample: most state changes land within 6 frames of the word.

Why these choices (all INFERRED):
- Blurred label: opens a question in the first second. Arrow forces gaze to it.
- Chart: the viewer's own analytics, so the problem is personal.
- Red question mark on the head: the literal idea of lost understanding.
- Glass tiles: calm, product-like, signal a system rather than a list.
- Red and white stage: the problem colour stays consistent across chart, avatar, brain and cone.
- Hawk: an odd word becomes memorable, and its flight path draws the "start high, go narrow" model, which then morphs into the cone. The transition teaches.
- Speaker looking up: directs the viewer's eyes to the clip and sells the reaction.
- Silence at 70-75: contrast makes the warning heavier.
- Green sweep on "eight most": moves the eye across all pages to show how much is included.
- Serif italic: marks the word to remember without changing colour.

## 11 Animation inventory

Format: ID, start-end, frames, scene type, script line, keyframes, rebuild.

- V4-A01, 0.04-0.67, 15 f, hook, "This is the best", word Best then Storytelling (0.29) then Hack (0.50), stagger about 5 f. F2 per word.
- V4-A02, 0.00-0.75, 18 f, hook, "This is the best storytelling", arrow draws down 0.0-0.46, head at about 0.33. Disc grows 0.08-0.25 then to about 305 px at 0.5, fades 0.42-0.75. SVG dash plus eased scale, opacity ramp.
- V4-A03, 1.46-1.63, 4 f, hook, "for", arrow and blurred label fade.
- V4-A04, 1.58-2.25, 16 f, hook, "educational", 5 phone tiles flicker in at 1.58, 1.71, 1.83, 2.00, 2.17. 3+2 layout. F1 style.
- V4-A05, 3.21-3.29, 2 f, hook, "content.", title fades before the cut.
- V4-A06, 3.83-3.96, 3 f, full, "Comprehension", serif caption fade in.
- V4-A07, 5.17-7.67, 60 f, chart, "The reason your retention chart looks like this", stage pan, F4.
- V4-A08, 5.17-7.90, 66 f, chart, same line, curve draw, about 12.9 px/f in the middle, ease-out from 7.4, length 623 px.
- V4-A09, 5.25-6.10, 20 f, chart, "The reason your", title words at 5.25, 5.46, 5.71, 5.92, line 2 at 5.58. F2.
- V4-A10, 6.50-9.00, 60 f, chart, "is because viewers", chart lift, F4.
- V4-A11, 7.44-8.45, 24 f, chart, "viewers", avatar fade in, brighten, `?` at 8.11.
- V4-A12, 7.75-8.10, 8 f, chart, "are", end dot grows with ring.
- V4-A13, 13.08-13.96, 21 f, tiles, "So here are the two", title stagger, tiles flicker (1 at 13.08, 2 at 13.17), numerals 13.50 and 13.63.
- V4-A14, 13.42-14.50, 26 f, tiles, sheen runs round tile rim.
- V4-A15, 14.17-14.83, 16 f, tiles, "hacks", stems draw upward from tile tops.
- V4-A16, 14.83-15.25, 10 f, tiles, "Comprehension", parent label fades in, bracket joins.
- V4-A17, 13.1-16.2, 74 f, tiles, slow push-in, about 17 percent.
- V4-A18, 16.29-16.71, 10 f, tiles, "The first", stage pan with blur, tile 2 and label leave right, tile 1 reaches centre.
- V4-A19, 17.21-17.42, 5 f, tiles, "visual", numeral to eye icon, label below. F1 style.
- V4-A20, 18.25-19.75, 36 f, dock, "It sounds obvious", F3. Old title leaves top at about 18.6.
- V4-A21, 19.29-19.58, 7 f, clip, "the visuals", stroke first at 19.29, then window F1.
- V4-A22, 19.58-22.08, 60 f, clip, window rises 60 px, ease-out.
- V4-A23, 20.83-21.50, 16 f, clip, "don't pair", link icon flicker on, pill below, link breaks into two halves at about 21.5.
- V4-A24, 21.83-23.00, 28 f, clip, "words being said", waveform runs in pill, sheen on pill edge.
- V4-A25, 22.50-23.25, 18 f, clip, "said, the", F5.
- V4-A26, 23.25-25.42, 52 f, brain, "comprehension is gonna decay", fill falls, hue green to red, brain rotates.
- V4-A27, 25.42-25.67, 6 f, brain to preview, "fast. Look", brain dims and returns once, clip fades in. Flicker dissolve.
- V4-A28, 27.38-27.67, 7 f, clip, "Behind", feather replaced by crisp window, bar F1.
- V4-A29, 27.54-39.5, 287 f, clip, Mr.Beast speech, linear bar fill.
- V4-A30, 39.37-39.46, 3 f, clip, "$500,000.", bar fades.
- V4-A31, 39.50-40.58, 26 f, grid, "Every single visual", 9 tiles, 3 f stagger.
- V4-A32, 49.63-50.46, 20 f, recall, "the second tip", tile 2 flicker, title stagger.
- V4-A33, 51.83-52.08, 6 f, recall, "hawk", numeral to logo, label at 51.92.
- V4-A34, 52.00-52.58, 14 f, recall, tile grows about 15 percent.
- V4-A35, 52.58-54.96, 57 f, dock, "When you storytell", F3 long tail, title leaves top.
- V4-A36, 54.96-55.25, 7 f, hawk, "hawk", hawk, arc, beam, dot flicker on.
- V4-A37, 55.00-58.83, 92 f, hawk, "hunting for food. You start super high", beam swings left to right, peak right about 57.0, back to vertical. About +/-25 degrees, INFERRED from frames.
- V4-A38, 59.00-59.17, 4 f, hawk, "you", beam fades.
- V4-A39, 59.13-59.67, 13 f, hawk, "dive", hawk rolls, red trail grows, path a tall loop.
- V4-A40, 59.67-60.25, 14 f, hawk, "down narrow", hawk falls straight to dot.
- V4-A41, 60.33-60.42, 2 f, hawk, "once", wings detach, dot jumps to mid frame, a smear frame. VERIFIED 60.33.
- V4-A42, 60.42-61.00, 14 f, ring, "you have a", ring expands to about 668 px, stroke thins, fades.
- V4-A43, 61.00-62.92, 46 f, ring, "focus point. The best storytelling", second ring 191 to 663 px, ease-out.
- V4-A44, 62.17-65.0, 68 f, cone, "delivered in the exact same way", cone scale from dot, height 408 at 63.33, 478 at 63.75, 530 at 64.17, 559 at 64.58, 586 at 65.0.
- V4-A45, 62.83-63.17, 8 f, cone, "exact", ring wipes off from top.
- V4-A46, 63.42-64.75, 32 f, cone, "way. Broad and high", red beam grows from tip, dot slides.
- V4-A47, 66.16-66.40, 6 f, cone, "First", label setup context appears.
- V4-A48, 66.16-66.74, 14 f, cone, "First,", red stroke draws both ways round ellipse from front.
- V4-A49, 68.26-68.40, 3 f, cone, "before", label point.
- V4-A50, 68.26-69.42, 28 f, cone, "before diving deeper", red segment runs from lip to tip on both sides.
- V4-A51, 75.46-77.46, 48 f, orbit, "improve your storytelling", 6 thumbnails orbit clockwise.
- V4-A52, 75.50-76.42, 22 f, orbit, "if you want to improve", brain fades in, colour grey-red to yellow to green.
- V4-A53, 77.50-78.33, 20 f, CTA, "comment story", words, banner, 9 doc tiles 2 f stagger, tiles grey for 2-3 f.
- V4-A54, 79.50-80.25, 19 f, CTA, "the eight most", green sweep, each tile peaks then decays.

## 12 Gaps and unknowns

Inspected at 24 fps: all layout boundaries, 0-3, 5-6.5, 13-14.5, 14.8-19.5, 19.5-21, 22.4-23.4, 27-28.5, 38.9-40.4, 49.5-51, 75.3-76.8.
Inspected at 8-12 fps: 6.5-10.4, 21-27, 40.2-43.2, 51-70.2, 76.8-82.2.
Inspected at 3.2 fps: 28.5-39.5.
Inspected at 1 fps only: 3.5-5, 10.6-13, 14.5-14.83, 43.2-49.5, 70.2-75.3, 82.2-89.83, plus per-frame difference data, which shows only hand motion at the peaks checked (4.2, 12.3, 48.8, 74.2, 84.3).

UNKNOWN:
- Actual fonts.
- Whether full-screen blocks contain morph cuts or silence removal. Head moves fast at 4.2 (f100-103), not proven.
- True source of the panel background.
- Exact panel-to-full-screen scale.
- 3D tool, and whether brain, hawk and cone are code or pre-rendered.
- SFX identities and music title.
- Exact count of embedded cuts near 36.04 and 38.3.
- Stem leakage: demucs output includes voice residue, so events under about -35 dB are unreliable.
