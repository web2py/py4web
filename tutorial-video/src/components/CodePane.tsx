import React from 'react';
import {useCurrentFrame, interpolate, Easing} from 'remotion';
import {theme} from './theme';
import {HighlightedPython} from './highlight';

export const CodePane: React.FC<{
  filename: string;
  code: string;
  width?: number | string;
  height?: number | string;
  fontSize?: number;
  /** Frame at which the pane appears */
  appearAt?: number;
  /** Reveal lines progressively from top to bottom over this many frames. */
  revealDuration?: number;
  /** Highlight a range of lines (1-indexed inclusive) */
  highlight?: [number, number];
  highlightAt?: number;
}> = ({
  filename,
  code,
  width = 1500,
  height = 760,
  fontSize = 24,
  appearAt = 0,
  revealDuration = 0,
  highlight,
  highlightAt = 0,
}) => {
  const frame = useCurrentFrame();
  const localFrame = frame - appearAt;

  if (localFrame < 0) return null;

  const lines = code.split('\n');
  const totalLines = lines.length;

  let visibleLines = totalLines;
  if (revealDuration > 0) {
    visibleLines = Math.ceil(
      interpolate(localFrame, [0, revealDuration], [0, totalLines], {
        extrapolateRight: 'clamp',
      })
    );
  }

  const visibleCode = lines.slice(0, visibleLines).join('\n');

  // Auto-scroll: keep the most-recently-revealed line in view by shifting
  // content upward when it exceeds the pane content area.
  const lineHeightPx = fontSize * 1.5;
  const PADDING_VERT = 24 * 2; // matches inner div padding 24px top/bottom
  const HEADER_PX = 44;
  const innerHeightPx =
    typeof height === 'number' ? height - HEADER_PX - PADDING_VERT : 0;
  const visibleHeightPx = visibleLines * lineHeightPx;
  const overflow = Math.max(0, visibleHeightPx - innerHeightPx);

  const intro = interpolate(localFrame, [0, 12], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.ease),
  });

  return (
    <div
      style={{
        width,
        height,
        background: theme.bgPanel,
        borderRadius: 14,
        boxShadow: '0 30px 80px rgba(0,0,0,0.5)',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
        opacity: intro,
        transform: `translateY(${(1 - intro) * 20}px)`,
      }}
    >
      <div
        style={{
          height: 44,
          background: theme.bgTerminal,
          display: 'flex',
          alignItems: 'center',
          padding: '0 18px',
          gap: 12,
          color: theme.textDim,
          fontFamily: theme.fontMono,
          fontSize: 16,
        }}
      >
        <span style={{color: theme.accent2, fontWeight: 600}}>📄</span>
        <span>{filename}</span>
      </div>
      <div
        style={{
          flex: 1,
          padding: '24px 32px',
          overflow: 'hidden',
          position: 'relative',
        }}
      >
        <div
          style={{
            transform: `translateY(${-overflow}px)`,
            transition: 'none',
            position: 'relative',
          }}
        >
          {highlight && frame >= highlightAt && (
            <HighlightOverlay
              lines={lines}
              range={highlight}
              fontSize={fontSize}
              opacity={interpolate(
                frame - highlightAt,
                [0, 10],
                [0, 1],
                {extrapolateRight: 'clamp'}
              )}
            />
          )}
          <HighlightedPython code={visibleCode} fontSize={fontSize} />
        </div>
      </div>
    </div>
  );
};

const HighlightOverlay: React.FC<{
  lines: string[];
  range: [number, number];
  fontSize: number;
  opacity: number;
}> = ({range, fontSize, opacity}) => {
  const lineHeight = fontSize * 1.5;
  const top = (range[0] - 1) * lineHeight;
  const height = (range[1] - range[0] + 1) * lineHeight;
  return (
    <div
      style={{
        position: 'absolute',
        left: -16,
        right: -16,
        top,
        height,
        background: 'rgba(255, 209, 102, 0.12)',
        borderLeft: `4px solid ${theme.yellow}`,
        borderRadius: 4,
        opacity,
      }}
    />
  );
};
