# py4web Todo Tutorial — Remotion Video

A ~2:22 captioned walkthrough of building the `apps/todo_tutorial/` app
(Auth + Form + Grid + JSON API, no JavaScript).

## Layout

```
src/
  index.ts            registerRoot
  Root.tsx            <Composition id="Main" .../>
  Main.tsx            timeline: intro → 6 chapters → outro
  components/
    theme.ts          colors / fonts
    highlight.tsx     tiny Python tokenizer + colorizer
    Terminal.tsx      animated zsh window (typing + output reveal)
    CodePane.tsx      animated code window (line-by-line reveal, optional highlight)
    Caption.tsx       lower-third caption with fade in/out
    SplitScene.tsx    ChapterScene wrapper (STEP NN + title bar)
    Intro.tsx         opening + closing cards
  chapters/
    Chapter1Setup.tsx     pip install / py4web setup / run
    Chapter2Clone.tsx     cp -r _scaffold todo_tutorial
    Chapter3Basic.tsx     models.py + controllers.py for the basic todo
    Chapter4Assign.tsx    extend the model with deadline + assigned_to + auth.signature
    Chapter5Views.tsx     three views via three different filters
    Chapter6Api.tsx       JSON endpoints + curl demo
```

## Run

```bash
npm install
npm start          # opens Remotion Studio at http://localhost:3000
npm run build      # renders out/py4web-todo-tutorial.mp4
```

## Knobs

- Composition is **1920×1080 @ 30 fps**, `MAIN_DURATION_FRAMES` in `src/Main.tsx`.
- Chapter durations are constants in `Main.tsx` — adjust to retime.
- Caption text is inline in each chapter file; edit & restart the studio.
- Code-reveal speed is the `revealDuration` prop on `<CodePane>`.
- Type-speed for terminal lines is `typeDuration` per `TerminalLine`.
