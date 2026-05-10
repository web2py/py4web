import React from 'react';
import {AbsoluteFill, Series} from 'remotion';
import {Intro, Outro} from './components/Intro';
import {Chapter1Setup} from './chapters/Chapter1Setup';
import {Chapter2Clone} from './chapters/Chapter2Clone';
import {Chapter3Basic} from './chapters/Chapter3Basic';
import {Chapter4Assign} from './chapters/Chapter4Assign';
import {Chapter5Views} from './chapters/Chapter5Views';
import {Chapter6Api} from './chapters/Chapter6Api';
import {theme} from './components/theme';

export const FPS = 30;
export const WIDTH = 1920;
export const HEIGHT = 1080;

const INTRO = 120; // 4s
const CH1 = 360; // 12s
const CH2 = 360; // 12s
const CH3 = 840; // 28s — two sub-scenes (model + controller)
const CH4 = 820; // ~27s — code + form screenshot
const CH5 = 1080; // 36s — code + grid screenshot
const CH6 = 940; // ~31s — api code + curl
const OUTRO = 150;

export const MAIN_DURATION_FRAMES =
  INTRO + CH1 + CH2 + CH3 + CH4 + CH5 + CH6 + OUTRO;

export const Main: React.FC = () => {
  return (
    <AbsoluteFill style={{background: theme.bg}}>
      <Series>
        <Series.Sequence durationInFrames={INTRO}>
          <Intro />
        </Series.Sequence>
        <Series.Sequence durationInFrames={CH1}>
          <Chapter1Setup />
        </Series.Sequence>
        <Series.Sequence durationInFrames={CH2}>
          <Chapter2Clone />
        </Series.Sequence>
        <Series.Sequence durationInFrames={CH3}>
          <Chapter3Basic />
        </Series.Sequence>
        <Series.Sequence durationInFrames={CH4}>
          <Chapter4Assign />
        </Series.Sequence>
        <Series.Sequence durationInFrames={CH5}>
          <Chapter5Views />
        </Series.Sequence>
        <Series.Sequence durationInFrames={CH6}>
          <Chapter6Api />
        </Series.Sequence>
        <Series.Sequence durationInFrames={OUTRO}>
          <Outro />
        </Series.Sequence>
      </Series>
    </AbsoluteFill>
  );
};
