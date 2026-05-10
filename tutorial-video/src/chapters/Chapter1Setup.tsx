import React from 'react';
import {Caption} from '../components/Caption';
import {Terminal, TerminalLine} from '../components/Terminal';
import {ChapterScene} from '../components/SplitScene';

const lines: TerminalLine[] = [
  {kind: 'cmd', text: 'pip install py4web', appearAt: 8, typeDuration: 30},
  {kind: 'out', text: 'Successfully installed py4web-1.20260403.2', appearAt: 60},
  {kind: 'spacer', appearAt: 70},
  {kind: 'cmd', text: 'py4web setup apps', appearAt: 90, typeDuration: 22},
  {kind: 'out', text: 'apps directory ready', appearAt: 130},
  {kind: 'spacer', appearAt: 140},
  {kind: 'cmd', text: 'py4web set_password', appearAt: 165, typeDuration: 26},
  {kind: 'out', text: 'Password stored in password.txt', appearAt: 210},
  {kind: 'spacer', appearAt: 220},
  {kind: 'cmd', text: 'py4web run apps', appearAt: 245, typeDuration: 22},
  {kind: 'out', text: 'Listening on http://127.0.0.1:8000/', appearAt: 290},
  {kind: 'out', text: 'Dashboard at /_dashboard', appearAt: 305},
];

export const Chapter1Setup: React.FC = () => {
  return (
    <ChapterScene step={1} title="Install &amp; run">
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Terminal title="zsh — install py4web" lines={lines} width={1500} height={680} />
      </div>
      <Caption
        text="Install with pip, scaffold an apps folder, and start the dev server."
        appearAt={6}
        duration={150}
      />
      <Caption
        text="The dashboard at /_dashboard manages every app you install."
        appearAt={250}
        duration={120}
      />
    </ChapterScene>
  );
};
