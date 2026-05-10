import React from 'react';
import {theme} from './theme';

const PYTHON_KEYWORDS = new Set([
  'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
  'while', 'with', 'yield',
]);

const PYTHON_BUILTINS = new Set([
  'print', 'dict', 'list', 'tuple', 'set', 'str', 'int', 'float', 'bool',
  'len', 'range', 'isinstance', 'self', 'cls',
]);

type Token = {type: string; value: string};

const tokenizePython = (src: string): Token[] => {
  const tokens: Token[] = [];
  let i = 0;
  while (i < src.length) {
    const ch = src[i];
    // comment
    if (ch === '#') {
      let j = i;
      while (j < src.length && src[j] !== '\n') j++;
      tokens.push({type: 'comment', value: src.slice(i, j)});
      i = j;
      continue;
    }
    // triple string
    if (
      (src.startsWith('"""', i) || src.startsWith("'''", i))
    ) {
      const quote = src.slice(i, i + 3);
      let j = i + 3;
      while (j < src.length && !src.startsWith(quote, j)) j++;
      j = Math.min(j + 3, src.length);
      tokens.push({type: 'string', value: src.slice(i, j)});
      i = j;
      continue;
    }
    // single string
    if (ch === '"' || ch === "'") {
      const quote = ch;
      let j = i + 1;
      while (j < src.length && src[j] !== quote) {
        if (src[j] === '\\') j++;
        j++;
      }
      j = Math.min(j + 1, src.length);
      tokens.push({type: 'string', value: src.slice(i, j)});
      i = j;
      continue;
    }
    // decorator
    if (ch === '@') {
      let j = i + 1;
      while (j < src.length && /[A-Za-z0-9_.]/.test(src[j])) j++;
      tokens.push({type: 'decorator', value: src.slice(i, j)});
      i = j;
      continue;
    }
    // number
    if (/[0-9]/.test(ch)) {
      let j = i;
      while (j < src.length && /[0-9.]/.test(src[j])) j++;
      tokens.push({type: 'number', value: src.slice(i, j)});
      i = j;
      continue;
    }
    // identifier
    if (/[A-Za-z_]/.test(ch)) {
      let j = i;
      while (j < src.length && /[A-Za-z0-9_]/.test(src[j])) j++;
      const word = src.slice(i, j);
      let type = 'plain';
      if (PYTHON_KEYWORDS.has(word)) type = 'keyword';
      else if (PYTHON_BUILTINS.has(word)) type = 'builtin';
      tokens.push({type, value: word});
      i = j;
      continue;
    }
    // whitespace or other
    tokens.push({type: 'plain', value: ch});
    i++;
  }
  return tokens;
};

const colorFor = (type: string) => {
  switch (type) {
    case 'comment':
      return theme.comment;
    case 'string':
      return theme.string;
    case 'keyword':
      return theme.keyword;
    case 'number':
      return theme.number;
    case 'builtin':
      return theme.builtin;
    case 'decorator':
      return theme.decorator;
    default:
      return theme.text;
  }
};

export const HighlightedPython: React.FC<{
  code: string;
  fontSize?: number;
  lineHeight?: number;
}> = ({code, fontSize = 28, lineHeight = 1.5}) => {
  const tokens = tokenizePython(code);
  return (
    <pre
      style={{
        margin: 0,
        fontFamily: theme.fontMono,
        fontSize,
        lineHeight,
        color: theme.text,
        whiteSpace: 'pre',
      }}
    >
      {tokens.map((t, idx) => (
        <span key={idx} style={{color: colorFor(t.type)}}>
          {t.value}
        </span>
      ))}
    </pre>
  );
};
