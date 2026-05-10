import React from 'react';
import {Series} from 'remotion';
import {Caption} from '../components/Caption';
import {CodePane} from '../components/CodePane';
import {ChapterScene} from '../components/SplitScene';
import {Screenshot} from '../components/Screenshot';

const modelCode = `# models.py
from pydal.validators import IS_NOT_EMPTY, IS_DATETIME, IS_IN_DB
from .common import Field, auth, db

db.define_table(
    "task",
    Field("description", "string", requires=IS_NOT_EMPTY()),
    Field("deadline", "datetime", requires=IS_DATETIME()),
    Field("completed", "boolean", default=False),
    Field(
        "assigned_to",
        "reference auth_user",
        requires=IS_IN_DB(db, "auth_user.id", "%(username)s"),
    ),
    auth.signature,   # adds created_by, created_on, modified_by, modified_on
)
db.commit()
`;

const SceneCode: React.FC = () => (
  <ChapterScene step={4} title="Assign tasks &amp; deadlines">
    <CodePane
      filename="apps/todo_tutorial/models.py"
      code={modelCode}
      fontSize={24}
      revealDuration={180}
      highlight={[7, 13]}
      highlightAt={220}
    />
    <Caption
      text="Add a deadline and an assignee. assigned_to references auth_user."
      appearAt={30}
      duration={200}
    />
    <Caption
      text="auth.signature gives you the assigner: created_by tracks who made the task."
      appearAt={260}
      duration={210}
    />
  </ChapterScene>
);

const SceneScreenshot: React.FC = () => (
  <ChapterScene step={4} title="…and Form just works" alignTop>
    <Screenshot
      src="todo2.png"
      url="127.0.0.1:8000/todo_tutorial/my_tasks?mode=edit&id=1"
      width={760}
      height={760}
    />
    <Caption
      text="The same Form() now renders Description, Deadline, Completed, Assigned To — plus auth.signature fields read-only."
      appearAt={20}
      duration={240}
    />
  </ChapterScene>
);

export const Chapter4Assign: React.FC = () => {
  return (
    <Series>
      <Series.Sequence durationInFrames={520}>
        <SceneCode />
      </Series.Sequence>
      <Series.Sequence durationInFrames={300}>
        <SceneScreenshot />
      </Series.Sequence>
    </Series>
  );
};

export const CHAPTER4_DURATION = 820;
