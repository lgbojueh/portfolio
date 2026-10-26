from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

start_marker = 'window.portfolioProjects = ['
start = text.index(start_marker) + len(start_marker)
end = text.index('\n];', start)
body = text[start:end]

# Parse top-level project objects while ignoring braces inside strings.
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
            objects.append(body[obj_start:i + 1].strip())
            obj_start = None


def get_title(block: str) -> str:
    match = re.search(r'title:\s*"([^"]+)"', block)
    return match.group(1) if match else ''

# Clean up Game Groove's public naming if the old mock name is still present.
for idx, block in enumerate(objects):
    if get_title(block) == 'Game Groove Mock':
        block = block.replace('title: "Game Groove Mock"', 'title: "Game Groove"', 1)
        block = block.replace('label: "Frontend Game Discovery App"', 'label: "Full-Stack Board Game Discovery"', 1)
        block = block.replace(
            '"TypeScript frontend mock application for exploring and presenting board game content through a clean interactive interface."',
            '"Full-stack board game discovery application with search, game details, saved favorites, authentication, and database-backed user features."',
            1,
        )
        objects[idx] = block

# Add Gatehouse only if it is not already present.
if not any(get_title(block) == 'Gatehouse IAM' for block in objects):
    objects.append('''{
    title: "Gatehouse IAM",
    label: "Identity & Access Management",

    description:
      "Security-focused full-stack application implementing authentication, server-side RBAC, protected administrator workflows, and audit logging across user, analyst, and admin roles.",

    tech: [
      "React",
      "TypeScript",
      "FastAPI",
      "JWT",
      "RBAC",
      "Docker"
    ],

    repo:
      "https://github.com/lgbojueh/gatehouse-iam",

    lat: 38.9072,
    lon: -77.0369,
    color: 0x8b5cf6
  }''')

priority = [
    'SignalDesk AI',
    'Game Groove',
    'Gatehouse IAM',
    'Docker Deployment Lab',
    'IT Support Diagnostic Dashboard',
    'Password Vault',
    'Portfolio Website',
]
rank = {title: i for i, title in enumerate(priority)}
objects = sorted(enumerate(objects), key=lambda item: (rank.get(get_title(item[1]), 1000 + item[0])))
objects = [block for _, block in objects]

new_body = '\n\n  ' + ',\n\n  '.join(objects) + '\n'
text = text[:start] + new_body + text[end:]

# Make the skills section reflect the stronger full-stack portfolio.
text = text.replace(
'''      <h4>Web Development</h4>
      <ul>
        <li>HTML / CSS</li>
        <li>React</li>
        <li>Node.js</li>
        <li>REST APIs</li>
        <li>Responsive Design</li>
      </ul>''',
'''      <h4>Web & APIs</h4>
      <ul>
        <li>React / Next.js</li>
        <li>TypeScript</li>
        <li>FastAPI</li>
        <li>Node.js / REST APIs</li>
        <li>Responsive Design</li>
      </ul>''',
1,
)

text = text.replace(
'''      <h4>Infrastructure</h4>
      <ul>
        <li>Docker</li>
        <li>Nginx</li>
        <li>PostgreSQL</li>
        <li>Redis</li>
        <li>Linux</li>
      </ul>''',
'''      <h4>Infrastructure</h4>
      <ul>
        <li>Docker</li>
        <li>Linux</li>
        <li>PostgreSQL</li>
        <li>GitHub Actions / CI</li>
        <li>Nginx / Redis</li>
      </ul>''',
1,
)

path.write_text(text, encoding='utf-8')
print('Portfolio updated with Gatehouse IAM and featured project ordering.')
