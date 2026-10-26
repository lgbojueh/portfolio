from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

start_marker = 'window.portfolioProjects = ['
start = text.index(start_marker) + len(start_marker)
end = text.index('\n];', start)
body = text[start:end]

objects = []
depth = 0
in_string = False
escape = False
obj_start = None
for i, ch in enumerate(body):
    if in_string:
        if escape:
            escape = False
        elif ch == '\\':
            escape = True
        elif ch == '"':
            in_string = False
        continue
    if ch == '"':
        in_string = True
        continue
    if ch == '{':
        if depth == 0:
            obj_start = i
        depth += 1
    elif ch == '}':
        depth -= 1
        if depth == 0 and obj_start is not None:
            objects.append(body[obj_start:i+1].strip())
            obj_start = None

def title(block):
    m = re.search(r'title:\s*"([^"]+)"', block)
    return m.group(1) if m else ''

new_projects = [
'''{
    title: "Language Parser & Interpreter",
    label: "Programming Languages / Interpreter",
    description:
      "Python interpreter built from scratch with a hand-written lexer, recursive-descent parser, explicit AST, execution engine, control flow, and structured runtime errors.",
    tech: ["Python", "Lexer", "Parser", "AST", "Interpreter", "Pytest"],
    repo: "https://github.com/lgbojueh/language-parser-interpreter",
    lat: 42.3601,
    lon: -71.0589,
    color: 0x06b6d4
  }''',
'''{
    title: "Static Analysis / AST Tool",
    label: "Program Analysis CLI",
    description:
      "Python static-analysis CLI that inspects source code without executing it, extracting program structure, complexity metrics, and structured JSON/CSV reports using the standard-library AST.",
    tech: ["Python", "AST", "CLI", "JSON", "CSV", "Pytest"],
    repo: "https://github.com/lgbojueh/static-analysis-ast-tool",
    lat: 37.7749,
    lon: -122.4194,
    color: 0xf59e0b
  }'''
]

existing_titles = {title(block) for block in objects}
for block in new_projects:
    if title(block) not in existing_titles:
        objects.append(block)

priority = [
    'SignalDesk AI',
    'Game Groove',
    'Language Parser & Interpreter',
    'Static Analysis / AST Tool',
    'Gatehouse IAM',
    'Docker Deployment Lab',
    'IT Support Diagnostic Dashboard',
    'Password Vault',
    'Portfolio Website',
]
rank = {name: i for i, name in enumerate(priority)}
objects = [block for _, block in sorted(enumerate(objects), key=lambda item: (rank.get(title(item[1]), 1000 + item[0])))]

new_body = '\n\n  ' + ',\n\n  '.join(objects) + '\n'
text = text[:start] + new_body + text[end:]
path.write_text(text, encoding='utf-8')
print('Added parser and static analysis projects to portfolio.')
