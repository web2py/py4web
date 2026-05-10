import React from 'react';
import {Composition} from 'remotion';
import {Main, MAIN_DURATION_FRAMES, FPS, WIDTH, HEIGHT} from './Main';

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="Main"
        component={Main}
        durationInFrames={MAIN_DURATION_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
    </>
  );
};
