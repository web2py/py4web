import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate, Easing} from 'remotion';
import {theme} from './theme';

export const ChapterTitle: React.FC<{
  number: number;
  title: string;
  subtitle?: string;
}> = ({number, title, subtitle}) => {
  const frame = useCurrentFrame();
  const intro = interpolate(frame, [0, 18], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const slide = interpolate(frame, [0, 18], [60, 0], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill
      style={{
        background: theme.bg,
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
      }}
    >
      <div
        style={{
          opacity: intro,
          transform: `translateY(${slide}px)`,
          textAlign: 'center',
        }}
      >
        <div
          style={{
            color: theme.accent,
            fontFamily: theme.fontMono,
            fontSize: 36,
            letterSpacing: 6,
            marginBottom: 24,
          }}
        >
          STEP {String(number).padStart(2, '0')}
        </div>
        <div
          style={{
            color: theme.text,
            fontFamily: theme.fontSans,
            fontSize: 100,
            fontWeight: 700,
            letterSpacing: -1,
            maxWidth: 1700,
            lineHeight: 1.1,
          }}
        >
          {title}
        </div>
        {subtitle && (
          <div
            style={{
              color: theme.textDim,
              fontFamily: theme.fontSans,
              fontSize: 38,
              marginTop: 28,
              maxWidth: 1500,
              marginLeft: 'auto',
              marginRight: 'auto',
            }}
          >
            {subtitle}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
