import React from 'react';
import {useCurrentFrame, interpolate, Easing} from 'remotion';
import {theme} from './theme';

export const Caption: React.FC<{
  text: string;
  appearAt: number;
  duration: number;
}> = ({text, appearAt, duration}) => {
  const frame = useCurrentFrame();
  const local = frame - appearAt;

  if (local < 0 || local > duration) return null;

  const intro = interpolate(local, [0, 12], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.ease),
  });
  const outro = interpolate(local, [duration - 12, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const opacity = Math.min(intro, outro);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 60,
        left: 0,
        right: 0,
        display: 'flex',
        justifyContent: 'center',
        opacity,
        transform: `translateY(${(1 - intro) * 16}px)`,
      }}
    >
      <div
        style={{
          background: 'rgba(13, 27, 42, 0.92)',
          color: theme.text,
          fontFamily: theme.fontSans,
          fontSize: 36,
          fontWeight: 500,
          padding: '14px 32px',
          borderRadius: 12,
          maxWidth: 1500,
          textAlign: 'center',
          border: `1px solid ${theme.accent}40`,
          boxShadow: '0 8px 28px rgba(0,0,0,0.4)',
        }}
      >
        {text}
      </div>
    </div>
  );
};
