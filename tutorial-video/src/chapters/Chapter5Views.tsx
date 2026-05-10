import React from 'react';
import {Series} from 'remotion';
import {Caption} from '../components/Caption';
import {CodePane} from '../components/CodePane';
import {ChapterScene} from '../components/SplitScene';
import {Screenshot} from '../components/Screenshot';

const code = `# controllers.py
def _me():
    return auth.user_id

@action("my_tasks")
@action.uses("grid.html", db, session, auth.user, T)
def my_tasks():
    grid = Grid(
        db.task.assigned_to == _me(),
        columns=[db.task.description, db.task.deadline,
                 db.task.completed, db.task.created_by],
        editable=lambda row: row["created_by"] == _me(),
        deletable=lambda row: row["created_by"] == _me(),
    )
    return dict(grid=grid, title="My tasks")

@action("assigned")
@action.uses("grid.html", db, session, auth.user, T)
def assigned():
    grid = Grid(
        (db.task.created_by == _me()) & (db.task.assigned_to != _me()),
        create=True, editable=True, deletable=True,
    )
    return dict(grid=grid, title="Tasks I assigned")

@action("by_others")
@action.uses("grid.html", db, session, auth.user, T)
def by_others():
    grid = Grid(
        (db.task.assigned_to == _me()) & (db.task.created_by != _me()),
        create=False, editable=False, deletable=False,
    )
    return dict(grid=grid, title="Tasks others assigned to me")
`;

const SceneCode: React.FC = () => (
  <ChapterScene step={5} title="Three views, one query each">
    <CodePane
      filename="apps/todo_tutorial/controllers.py"
      code={code}
      fontSize={20}
      revealDuration={260}
    />
    <Caption
      text="Each view is a different filter on the same table."
      appearAt={30}
      duration={200}
    />
    <Caption
      text="my_tasks: assigned to me. assigned: I created. by_others: assigned to me by someone else."
      appearAt={250}
      duration={220}
    />
    <Caption
      text="editable / deletable accept booleans, URLs, or per-row callables."
      appearAt={500}
      duration={210}
    />
  </ChapterScene>
);

const SceneScreenshot: React.FC = () => (
  <ChapterScene step={5} title="…rendered by Grid" alignTop>
    <Screenshot
      src="todo1.png"
      url="127.0.0.1:8000/todo_tutorial/my_tasks"
      width={1200}
      height={740}
    />
    <Caption
      text="Search, sort, paginate, and per-row Details / Edit / Delete buttons — all from one Grid() call."
      appearAt={20}
      duration={240}
    />
  </ChapterScene>
);

export const Chapter5Views: React.FC = () => {
  return (
    <Series>
      <Series.Sequence durationInFrames={780}>
        <SceneCode />
      </Series.Sequence>
      <Series.Sequence durationInFrames={300}>
        <SceneScreenshot />
      </Series.Sequence>
    </Series>
  );
};

export const CHAPTER5_DURATION = 1080;
