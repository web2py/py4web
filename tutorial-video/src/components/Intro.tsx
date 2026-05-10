import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate, Easing} from 'remotion';
import {theme} from './theme';

export const Intro: React.FC = () => {
  const frame = useCurrentFrame();

  const titleIntro = interpolate(frame, [10, 35], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const subIntro = interpolate(frame, [25, 50], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const slide = interpolate(frame, [10, 35], [40, 0], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(circle at 30% 30%, ${theme.bgPanel}, ${theme.bg})`,
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
      }}
    >
      <div
        style={{
          textAlign: 'center',
          opacity: titleIntro,
          transform: `translateY(${slide}px)`,
        }}
      >
        <div
          style={{
            color: theme.accent2,
            fontFamily: theme.fontMono,
            fontSize: 40,
            letterSpacing: 8,
            marginBottom: 28,
          }}
        >
          py4web tutorial
        </div>
        <div
          style={{
            color: theme.text,
            fontFamily: theme.fontSans,
            fontSize: 130,
            fontWeight: 800,
            letterSpacing: -2,
          }}
        >
          Build a Todo App
        </div>
        <div
          style={{
            color: theme.text,
            fontFamily: theme.fontSans,
            fontSize: 70,
            fontWeight: 400,
            marginTop: 18,
            opacity: subIntro,
          }}
        >
          with Auth, Form, Grid &amp; an API
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const intro = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill
      style={{
        background: theme.bg,
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <div style={{textAlign: 'center', opacity: intro}}>
        <div
          style={{
            color: theme.text,
            fontFamily: theme.fontSans,
            fontSize: 110,
            fontWeight: 800,
          }}
        >
          That's it.
        </div>
        <div
          style={{
            color: theme.textDim,
            fontFamily: theme.fontSans,
            fontSize: 50,
            marginTop: 30,
          }}
        >
          A full todo app — Auth, Form, Grid, API — in ~80 lines.
        </div>
        <div
          style={{
            color: theme.accent2,
            fontFamily: theme.fontMono,
            fontSize: 36,
            marginTop: 60,
          }}
        >
          py4web.com
        </div>
      </div>
    </AbsoluteFill>
  );
};
