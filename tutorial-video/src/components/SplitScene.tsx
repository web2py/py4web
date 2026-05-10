import React from 'react';
import {AbsoluteFill} from 'remotion';
import {theme} from './theme';

/**
 * A scene with a title row at the top and a content area below.
 * Used to give every chapter a consistent header.
 */
export const ChapterScene: React.FC<{
  step: number;
  title: string;
  children: React.ReactNode;
  alignTop?: boolean;
}> = ({step, title, children, alignTop = false}) => {
  return (
    <AbsoluteFill style={{background: theme.bg}}>
      <div
        style={{
          padding: '40px 80px 0',
          display: 'flex',
          alignItems: 'baseline',
          gap: 32,
        }}
      >
        <div
          style={{
            color: theme.accent,
            fontFamily: theme.fontMono,
            fontSize: 28,
            letterSpacing: 4,
          }}
        >
          STEP {String(step).padStart(2, '0')}
        </div>
        <div
          style={{
            color: theme.text,
            fontFamily: theme.fontSans,
            fontSize: 52,
            fontWeight: 700,
          }}
        >
          {title}
        </div>
      </div>
      <div
        style={{
          flex: 1,
          display: 'flex',
          alignItems: alignTop ? 'flex-start' : 'center',
          justifyContent: 'center',
          padding: '20px 80px 80px',
        }}
      >
        {children}
      </div>
    </AbsoluteFill>
  );
};
