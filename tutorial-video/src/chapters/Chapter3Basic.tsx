import React from 'react';
import {Series} from 'remotion';
import {Caption} from '../components/Caption';
import {CodePane} from '../components/CodePane';
import {ChapterScene} from '../components/SplitScene';

const modelCode = `# models.py
from pydal.validators import IS_NOT_EMPTY
from .common import Field, db

db.define_table(
    "task",
    Field("description", "string", requires=IS_NOT_EMPTY()),
    Field("completed", "boolean", default=False),
)

db.commit()
`;

const controllerCode = `# controllers.py
from py4web import action, URL, redirect
from py4web.utils.form import Form
from py4web.utils.grid import Grid

from .common import auth, db, session, T

@action("index")
@action.uses("grid.html", db, session, auth.user, T)
def index():
    grid = Grid(
        db.task,
        columns=[db.task.description, db.task.completed],
    )
    return dict(grid=grid, title="My todos")
`;

const SceneModel: React.FC = () => (
  <ChapterScene step={3} title="A single-page todo">
    <CodePane
      filename="apps/todo_tutorial/models.py"
      code={modelCode}
      fontSize={28}
      revealDuration={120}
    />
    <Caption
      text="Define one table. PyDAL handles migrations."
      appearAt={20}
      duration={160}
    />
    <Caption
      text="db.commit() persists the schema."
      appearAt={220}
      duration={150}
    />
  </ChapterScene>
);

const SceneController: React.FC = () => (
  <ChapterScene step={3} title="A single-page todo">
    <CodePane
      filename="apps/todo_tutorial/controllers.py"
      code={controllerCode}
      fontSize={26}
      revealDuration={140}
    />
    <Caption
      text="One action. Grid renders the list — no JavaScript needed."
      appearAt={20}
      duration={180}
    />
    <Caption
      text="@action.uses declares fixtures: template, db, session, login."
      appearAt={230}
      duration={170}
    />
  </ChapterScene>
);

export const Chapter3Basic: React.FC = () => {
  return (
    <Series>
      <Series.Sequence durationInFrames={420}>
        <SceneModel />
      </Series.Sequence>
      <Series.Sequence durationInFrames={420}>
        <SceneController />
      </Series.Sequence>
    </Series>
  );
};

export const CHAPTER3_DURATION = 840;
