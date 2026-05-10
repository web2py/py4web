import React from 'react';
import {Caption} from '../components/Caption';
import {Terminal, TerminalLine} from '../components/Terminal';
import {ChapterScene} from '../components/SplitScene';

const lines: TerminalLine[] = [
  {kind: 'cmd', text: 'cp -r apps/_scaffold apps/todo_tutorial', appearAt: 6, typeDuration: 40},
  {kind: 'out', text: '', appearAt: 60},
  {kind: 'cmd', text: 'ls apps/todo_tutorial', appearAt: 80, typeDuration: 22},
  {kind: 'out', text: 'common.py        models.py        settings.py', appearAt: 120},
  {kind: 'out', text: 'controllers.py   tasks.py         static/', appearAt: 132},
  {kind: 'out', text: '__init__.py      templates/       translations/', appearAt: 144},
  {kind: 'spacer', appearAt: 156},
  {kind: 'out', text: '# every app is just a Python package — copy & customize', appearAt: 180},
];

export const Chapter2Clone: React.FC = () => {
  return (
    <ChapterScene step={2} title="Clone the scaffold">
      <Terminal title="zsh — clone _scaffold" lines={lines} width={1500} height={620} fontSize={26} />
      <Caption
        text="_scaffold is the starter template. Copy it; you have a working app."
        appearAt={6}
        duration={170}
      />
      <Caption
        text="common.py wires Auth & DB. models.py is where your tables go. controllers.py is your routes."
        appearAt={200}
        duration={130}
      />
    </ChapterScene>
  );
};
