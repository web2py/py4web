import React from 'react';
import {AbsoluteFill, useCurrentFrame, interpolate} from 'remotion';
import {theme} from './theme';

export type TerminalLine =
  | {kind: 'cmd'; text: string; appearAt: number; typeDuration?: number}
  | {kind: 'out'; text: string; appearAt: number}
  | {kind: 'spacer'; appearAt: number};

export const Terminal: React.FC<{
  title?: string;
  lines: TerminalLine[];
  width?: number | string;
  height?: number | string;
  fontSize?: number;
}> = ({
  title = 'bash',
  lines,
  width = 1500,
  height = 760,
  fontSize = 26,
}) => {
  const frame = useCurrentFrame();

  return (
    <div
      style={{
        width,
        height,
        background: theme.bgTerminal,
        borderRadius: 14,
        boxShadow: '0 30px 80px rgba(0,0,0,0.5)',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
        border: `1px solid ${theme.bgPanel}`,
      }}
    >
      {/* title bar */}
      <div
        style={{
          height: 40,
          background: theme.bgPanel,
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
            color: theme.textDim,
            fontFamily: theme.fontMono,
            marginLeft: 16,
            fontSize: 16,
          }}
        >
          {title}
        </div>
      </div>
      {/* body */}
      <div
        style={{
          flex: 1,
          padding: '20px 28px',
          fontFamily: theme.fontMono,
          fontSize,
          lineHeight: 1.5,
          color: theme.text,
          overflow: 'hidden',
        }}
      >
        {lines.map((line, idx) => (
          <TerminalLineRow key={idx} line={line} frame={frame} />
        ))}
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

const TerminalLineRow: React.FC<{line: TerminalLine; frame: number}> = ({
  line,
  frame,
}) => {
  if (frame < line.appearAt) return null;

  if (line.kind === 'spacer') {
    return <div style={{height: '0.6em'}} />;
  }

  if (line.kind === 'out') {
    const opacity = interpolate(
      frame - line.appearAt,
      [0, 6],
      [0, 1],
      {extrapolateRight: 'clamp'}
    );
    return (
      <div style={{opacity, color: theme.textDim, whiteSpace: 'pre'}}>
        {line.text}
      </div>
    );
  }

  // cmd: animated typing
  const duration = line.typeDuration ?? Math.max(20, line.text.length * 1.2);
  const progress = interpolate(
    frame - line.appearAt,
    [0, duration],
    [0, line.text.length],
    {extrapolateRight: 'clamp'}
  );
  const typed = line.text.slice(0, Math.floor(progress));
  const stillTyping = progress < line.text.length;

  return (
    <div style={{whiteSpace: 'pre'}}>
      <span style={{color: theme.prompt}}>$ </span>
      <span style={{color: theme.text}}>{typed}</span>
      {stillTyping ? (
        <span
          style={{
            display: 'inline-block',
            width: '0.55em',
            height: '1em',
            background: theme.accent,
            verticalAlign: 'text-bottom',
          }}
        />
      ) : null}
    </div>
  );
};

export const TerminalChapter: React.FC<{
  title?: string;
  lines: TerminalLine[];
}> = ({title, lines}) => {
  return (
    <AbsoluteFill
      style={{
        background: theme.bg,
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Terminal title={title} lines={lines} />
    </AbsoluteFill>
  );
};
