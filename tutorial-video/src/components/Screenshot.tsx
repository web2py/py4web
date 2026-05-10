import React from 'react';
import {staticFile, useCurrentFrame, interpolate, Easing} from 'remotion';
import {theme} from './theme';

/**
 * A browser-style frame around a static screenshot.
 * The image fades + slides in, then sits centered.
 */
export const Screenshot: React.FC<{
  src: string;
  url: string;
  width?: number;
  height?: number;
}> = ({src, url, width = 1100, height = 880}) => {
  const frame = useCurrentFrame();
  const intro = interpolate(frame, [0, 18], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const lift = interpolate(frame, [0, 18], [40, 0], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  return (
    <div
      style={{
        opacity: intro,
        transform: `translateY(${lift}px)`,
        background: '#ffffff',
        borderRadius: 14,
        overflow: 'hidden',
        boxShadow: '0 30px 80px rgba(0,0,0,0.55)',
        width,
        height,
        display: 'flex',
        flexDirection: 'column',
        border: `1px solid ${theme.bgPanel}`,
      }}
    >
      {/* fake browser chrome */}
      <div
        style={{
          height: 44,
          background: '#1f2733',
          display: 'flex',
          alignItems: 'center',
          padding: '0 16px',
          gap: 8,
        }}
      >
        <Dot color="#ff5f56" />
        <Dot color="#ffbd2e" />
        <Dot color="#27c93f" />
        <div
          style={{
            background: '#0f1419',
            color: theme.textDim,
            fontFamily: theme.fontMono,
            fontSize: 16,
            padding: '4px 18px',
            borderRadius: 6,
            marginLeft: 24,
            flex: 1,
            textAlign: 'center',
            maxWidth: 760,
          }}
        >
          {url}
        </div>
      </div>
      <div
        style={{
          flex: 1,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          background: '#ffffff',
          overflow: 'hidden',
        }}
      >
        <img
          src={staticFile(src)}
          alt={url}
          style={{
            display: 'block',
            width: '100%',
            height: '100%',
            objectFit: 'contain',
            objectPosition: 'center',
          }}
        />
      </div>
    </div>
  );
};

const Dot: React.FC<{color: string}> = ({color}) => (
  <div
    style={{
      width: 14,
      height: 14,
      borderRadius: '50%',
      background: color,
    }}
  />
);
