import React from 'react';
import {Series} from 'remotion';
import {Caption} from '../components/Caption';
import {CodePane} from '../components/CodePane';
import {Terminal, TerminalLine} from '../components/Terminal';
import {ChapterScene} from '../components/SplitScene';

const code = `# controllers.py
@action("api/tasks", method="GET")
@action.uses(db, session, auth.user)
def api_list():
    me = _me()
    query = (db.task.assigned_to == me) | (db.task.created_by == me)
    rows = db(query).select(orderby=db.task.deadline)
    return dict(items=[r.as_dict() for r in rows])

@action("api/tasks", method="POST")
@action.uses(db, session, auth.user)
def api_create():
    res = db.task.validate_and_insert(**(request.json or {}))
    return dict(ok=not res.get("errors"), id=res.get("id"),
                errors=res.get("errors"))

@action("api/tasks/<task_id:int>", method="PUT")
@action.uses(db, session, auth.user)
def api_update(task_id):
    res = db(db.task.id == task_id).validate_and_update(**request.json)
    return dict(ok=bool(res.get("updated")))

@action("api/tasks/<task_id:int>", method="DELETE")
@action.uses(db, session, auth.user)
def api_delete(task_id):
    db(db.task.id == task_id).delete()
    return dict(ok=True)
`;

const curlLines: TerminalLine[] = [
  {kind: 'cmd', text: 'curl -X POST -H "Content-Type: application/json" \\', appearAt: 6, typeDuration: 50},
  {kind: 'cmd', text: '  -d \'{"description":"Buy milk","deadline":"2026-06-01 12:00","assigned_to":2}\' \\', appearAt: 60, typeDuration: 70},
  {kind: 'cmd', text: '  http://localhost:8000/todo_tutorial/api/tasks', appearAt: 135, typeDuration: 50},
  {kind: 'out', text: '{"ok": true, "id": 1}', appearAt: 200},
  {kind: 'spacer', appearAt: 215},
  {kind: 'cmd', text: 'curl http://localhost:8000/todo_tutorial/api/tasks', appearAt: 240, typeDuration: 60},
  {kind: 'out', text: '{', appearAt: 310},
  {kind: 'out', text: '  "items": [', appearAt: 320},
  {kind: 'out', text: '    {"id": 1, "description": "Buy milk", "completed": false,', appearAt: 332},
  {kind: 'out', text: '     "deadline": "2026-06-01T12:00:00", "assigned_to": 2}', appearAt: 344},
  {kind: 'out', text: '  ]', appearAt: 358},
  {kind: 'out', text: '}', appearAt: 366},
];

const SceneCode: React.FC = () => (
  <ChapterScene step={6} title="Add a JSON API">
    <CodePane
      filename="apps/todo_tutorial/controllers.py"
      code={code}
      fontSize={20}
      revealDuration={260}
    />
    <Caption
      text="Four endpoints: GET, POST, PUT, DELETE. The same db, session, auth fixtures."
      appearAt={30}
      duration={220}
    />
    <Caption
      text="validate_and_insert / validate_and_update apply the same validators as the form."
      appearAt={290}
      duration={200}
    />
  </ChapterScene>
);

const SceneCurl: React.FC = () => (
  <ChapterScene step={6} title="Add a JSON API">
    <Terminal
      title="zsh — exercising the API"
      lines={curlLines}
      width={1500}
      height={620}
      fontSize={22}
    />
    <Caption
      text="Same auth cookie protects both the HTML pages and the API."
      appearAt={20}
      duration={200}
    />
    <Caption
      text="No JS in the app. Just Auth, Form, Grid — and now JSON."
      appearAt={240}
      duration={170}
    />
  </ChapterScene>
);

export const Chapter6Api: React.FC = () => {
  return (
    <Series>
      <Series.Sequence durationInFrames={520}>
        <SceneCode />
      </Series.Sequence>
      <Series.Sequence durationInFrames={420}>
        <SceneCurl />
      </Series.Sequence>
    </Series>
  );
};

export const CHAPTER6_DURATION = 940;
